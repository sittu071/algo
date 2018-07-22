####################################################################################################
#   Name   :    execute_T1202.py                 Creation :  25/04/18                              #
####################################################################################################
#    Author :    Mausam Kumar Sinha                                                                #
####################################################################################################
import os
import re                             #Regular expression
import datetime
import subprocess                      #shell command line execution
from subprocess import Popen

#Exceptional handling: it will try to find the tet_lock and inside catch block will delete it.
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

currentworkingdirectory = os.getcwd()

def cleanup(): #delete the exsiting file if any
    if os.path.exists("temp.sh"):
        os.remove("temp.sh")

        #changing directory to /TETARUL/TestWareFs/T1202OSSCORE
    os.chdir(currentworkingdirectory)
        #Backup of old result file
    dest = "results_" + datetime.datetime.now().strftime("%y-%m-%d-%H:%M")
    os.rename("results", dest)
    os.mkdir("results")
    os.chmod(currentworkingdirectory + "/results", 777)
    try:
        findcmd = 'find . -name "tet_lock"' #looking for tet_lock if its there delete it
        out = subprocess.Popen(findcmd, shell=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Get standard out and error
        (stdout, stderr) = out.communicate()

        # Save found files to list
        filelist = stdout.decode().split()
        raise MyError(filelist[0])
    except MyError:
        print("")
        os.remove(filelist[0])
    except IndexError:
        pass


def startup(): #start the executing code
    if  os.path.isdir("/TETARUL"):
        os.chdir("/TETARUL")
    elif os.path.isdir("/TETSVN"):
        os.chdir("/TETSVN")
    else:
        print("Oops /TETSVN or /TETARUL directory not exist")

    currentdirectory = os.getcwd()
    if os.system(". ./setup.env"):
        print("setup environment successfully done")
    else:
        print("Not able to set environment variable try to do manually inside ", currentdirectory)
    os.chdir(currentworkingdirectory)
    currentdirectory = os.getcwd()
    print("Current Directory is ", currentdirectory)
    if os.system(". ./setup.env"):
        print("setup environment successfully done")
    else:
        print("Not able to set environment variable try do manually inside ", currentdirectory)
    tempvar = "export TET_EXECUTE=" + currentdirectory
    # exporting the current directory to make a tet executable
    if os.system(tempvar):
        print("TET_EXECUTE successfully exported")
    else:
        print("Not able to set TET_EXECUTE try to do manually inside  ", currentdirectory)
    print("Trying to find tet_scen file inside ", currentdirectory)
    path = "/usr/coreutils/bin:.:/bin:/usr/bin:/usr/ucb:/TETARUL/bin://bin:/usr/tandem/nssjava/jdk170_h70/bin"
    path = "export PATH=" + path
    os.system(path)

def mainmethod():

    with open('tet_scen', 'r') as file:
       array = []
       for line in file:
           if re.match(r'(\w)', line):
               array.append(line)
    with open("temp.sh", "a+") as file:
        os.system("chmod 777 temp.sh")
        file.write("#!/bin/sh")
        file.write("\n")

    length = len(array)
    for i in range(0, 1):
        cmd = "/TETARUL/bin/tcc -p -e $PWD " + array[i]
        with open("temp.sh", 'w+') as file:
            if re.match(r'\s\s+', cmd):
                pass
            else:
                file.write(cmd)
                file.close()
                parent_id = os.getpid()
                ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % parent_id, shell=True,
                                              stdout=subprocess.PIPE)
                ps_output = ps_command.stdout.read()
                retcode = ps_command.wait()
                for pid_str in ps_output.strip().split("\n")[:-1]:
                    print(int(pid_str))
                os.system("./temp.sh")
                print(os.getpid())


def result():
    os.chdir(currentworkingdirectory + "/results")
    os.system("cat `find . -name \\\"journal\\\"` > all_journal")
    os.system("/TETARUL/src/tet3/grw/grw -c beTIpfix all_journal > T1202COREUTILS.html")


#cleanup()
startup()
mainmethod()
result()
