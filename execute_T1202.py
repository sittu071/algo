######################################################################################################
#   Name   :    execute_T1202.py                 Creation :  25/04/18                                #
######################################################################################################
#    Author :    Mausam Kumar Sinha                                                                  #
######################################################################################################
#-------------------------------Authors Notes--------------------------------------------------------#
#this program has written in the sense of the user already set execute the setup env variable inside
#rootfolder and current directory, for any clarification feel free to ask at mausam-kumar.sinha@hpe.com

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


def mainmethod():
    with open('tet_scen', 'r') as file:
       array = []
       for line in file:
           if re.match(r'(\w)', line): #The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
               array.append(line)
    with open("temp.sh", "a+") as file:
        os.system("chmod 777 temp.sh")
        file.write("#!/bin/sh")
        file.write("\n")

    length = len(array)
    for i in range(0, 1):
        cmd = "/TETARUL/bin/tcc -p -e $PWD " + array[i]
        with open("temp.sh", 'w+') as file:
            if re.match(r'\s\s+', cmd): #The "\S" means Matches nonwhitespace.
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


def T1202Main_Fun():
    cleanup()
    mainmethod()
    result()


if __name__ == '__main__':
    T1202Main_Fun()



