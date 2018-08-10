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
import threading
import time
import multiprocessing
from subprocess import Popen
from concurrent.futures import ThreadPoolExecutor


#Exceptional handling: it will try to find the tet_lock and inside catch block will delete it.
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

threads = []
def cleanup(): #delete the exsiting file if any
    dest = "results_" + datetime.datetime.now().strftime("%y-%m-%d-%H:%M")#Backup of old result file
    os.rename("results", dest)
    os.mkdir("results")
    os.chmod("results", 777)
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

def threadFunction1(string):#crateing the thread for executing multiple process
    print(string,"  Thread is going to execute")
    os.system(string)
    time.sleep(5)

def mainmethod():
    with open('tet_scen', 'r') as file:
       array = []
       for line in file:
           if re.match(r'(\w)', line): #The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
               array.append(line)
    length = len(array)
    for i in range(0, length):
        cmd = "/TETARUL/bin/tcc -p -e $PWD " + array[i]
        print(cmd)
        #t1 = multiprocessing.Process(target=threadFunction1, args=(cmd,))
        #t1= threading.Thread(target=threadFunction1, args=(cmd,))
        #threads.append(t1)
        #threads[i].start()
        executor = ThreadPoolExecutor(max_workers=5)
        executor.submit(threadFunction1,cmd)
        time.sleep(5)
        #t1.daemon=True



def result():
    os.chdir("results")
    os.system("cat `find . -name \\\"journal\\\"` > all_journal")
    os.system("/TETARUL/src/tet3/grw/grw -c beTIpfix all_journal > T1202COREUTILS.html")


def T1202Main_Fun():
    t = time.time()
    cleanup()
    mainmethod()
    #result()
    t = time.time() -t
    print(t)

if __name__ == '__main__':
    T1202Main_Fun()



