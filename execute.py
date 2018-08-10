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
from threading import  Thread
import time
import Queue
from subprocess import Popen


queue = Queue.Queue()

#Exceptional handling: it will try to find the tet_lock and inside catch block will delete it.
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ThreadWorker(Thread): #Thread worker class is inherited from Thread class
    def __init__(self,queue): #constuctor of ThreadWorker class
        Thread.__init__(self) #constructor of Thread Class
        self.queue = queue #Initialisation of ThreadWorker queue
    def run(self): #It blocks thread until there is an item in the queue for the worker to process
        while True:
            var = self.queue.get()
            os.system(var)
            queue.task_done()


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


def mainmethod():
    with open('tet_scen', 'r') as file:
       array = []
       for line in file:
           if re.match(r'(\w)', line): #The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus underscore (_)
               array.append(line)
    length = len(array)
    #create 4 worker threads
    for x in range(4):
            worker = ThreadWorker(queue)
            # Setting daemon to True will let the main thread exit even though the workers are blocking
            worker.daemon = True
            worker.start()
    #put the tasks into a queue as a tuple
    for i in range(0, length):
        cmd = "/TETARUL/bin/tcc -p -e $PWD " + array[i] #this one is the task which we have to complete
        queue.put(cmd)
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()



def Main_Fun():
    t = time.time()
    cleanup()
    mainmethod()
    t = time.time() -t
    print(t)

if __name__ == '__main__':
    Main_Fun()



