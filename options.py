#!/usr/bin/env python
from pytet import *
from subprocess import Popen, PIPE, STDOUT
import os
import os.path
import shlex

def startup():
    print "Calling startup"

def cleanup():
    print "Calling cleanup"

def tet_infoline_output(output, return_code):
  tet_infoline ("Return code "+str(return_code))
  tet_infoline ("Output ")
  for i in output.split(os.linesep):
      tet_infoline(str(i).strip())

def tet_infoline_output_only(output):
  for i in output.split(os.linesep):
      tet_infoline(str(i).strip())

def compareSting(aList):
    found=False
    lMessage=[]
#    print aList[:-1]
#    print aList[-1]
    if os.path.exists(aList[-1].strip()):
        lMessage.append("File exists "+str(aList[-1].strip()))
        if os.path.isfile(aList[-1].strip()):
            lMessage.append("isFile "+str(os.path.isfile(aList[-1].strip())))
            lFile=open(aList[-1].strip(),"r").readlines()
            for aListcontent in aList[:-1]:
                found1=True
                for lFile1 in lFile:
                    if aListcontent in lFile1.strip():
                        lMessage.append(lFile1.strip()+str("::")+str(True))
                        found1=False
                        break
                if found1:
                    lMessage.append(aListcontent.strip()+str("::")+str(False))
    else:
        found=False
    print lMessage
    if any("::False" in s for s in lMessage):
        lMessage.append(1)
    else:
        lMessage.append(0)
    return lMessage

def writeToFile(str):
	fileName="output.file"
	with open(fileName,'w') as f:
		f.write(str)
	return fileName

def test1():
  tet_infoline ("Check the help /usr/bin/zipdetails --help")
  tet_infoline ("test define 1")
  tet_infoline ("Help /usr/bin/zipdetails --help")
  process = Popen(shlex.split("/usr/bin/zipdetails --help"), stdout=PIPE)
  exit_code = process.wait()
  if exit_code != 255:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  tet_result(TET_PASS)

def test2():
  tet_infoline ("Check the /usr/bin/zipdetails --h")
  tet_infoline ("test define 2")
  tet_infoline ("help /usr/bin/zipdetails --h ")
  process = Popen(shlex.split("/usr/bin/zipdetails --h"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["This program is free software; you can redistribute it and",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 255:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test3():
  tet_infoline ("/usr/bin/zipdetails --v")
  tet_infoline ("test define 3")
  tet_infoline ("/usr/bin/zipdetails --v")
  process = Popen(shlex.split("/usr/bin/zipdetails --v"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["This program is free software; you can redistribute it and",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 255:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test4():
  tet_infoline ("/usr/bin/xsubpp")
  tet_infoline ("Description functionality of /usr/bin/xsubpp")
  tet_infoline ("test define 4")
  tet_infoline ("/usr/bin/xsubpp")
  process = Popen(shlex.split("/usr/bin/xsubpp"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["file.xs",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 255:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return

  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test5():
  tet_infoline ("/usr/bin/xsubpp x.xs")
  tet_infoline ("Description functionality of /usr/bin/xsubpp x.xs")
  tet_infoline ("test define 5")
  tet_infoline ("/usr/bin/xsubpp x.xs")
  process = Popen(shlex.split("/usr/bin/xsubpp x.xs"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["cannot open x.xs: No such file or directory",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 162:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)

def test13():
  tet_infoline ("Check the /usr/bin/phpize --version")
  tet_infoline ("Description functionality of /usr/bin/phpize --version")
  tet_infoline ("test define 13")
  tet_infoline ("/usr/bin/phpize --version")
  process = Popen(shlex.split("/usr/bin/phpize --version"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["Configuring for","Zend Extension Api No:",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 0:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test14():
  tet_infoline ("Check the /usr/bin/shasum -h")
  tet_infoline ("Description functionality of /usr/bin/shasum -h")
  tet_infoline ("test define 14")
  tet_infoline ("/usr/bin/shasum -h")
  process = Popen(shlex.split("/usr/bin/shasum -h"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["The sums are computed as described in FIPS PUB 180-4",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 0:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test15():
  tet_infoline ("Check the /usr/bin/shasum -v")
  tet_infoline ("Description functionality of /usr/bin/shasum -v")
  tet_infoline ("test define 15")
  tet_infoline ("/usr/bin/shasum -v")
  process = Popen(shlex.split("/usr/bin/shasum -v"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["5.96",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 0:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)

def test16():
  tet_infoline ("Check the /usr/bin/shasum --version")
  tet_infoline ("Description functionality of /usr/bin/shasum --version")
  tet_infoline ("test define 16")
  tet_infoline ("/usr/bin/shasum --version")
  process = Popen(shlex.split("/usr/bin/shasum --version"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["5.96",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 0:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)
  
def test17():
  tet_infoline ("Check the /usr/bin/ptargrep --help")
  tet_infoline ("Description functionality of /usr/bin/ptargrep --help")
  tet_infoline ("test define 17")
  tet_infoline ("/usr/bin/ptargrep --help")
  process = Popen(shlex.split("/usr/bin/ptargrep --help"), stdout=PIPE)
  output, errors = process.communicate()
  exit_code = process.wait()
  tet_infoline_output(output,exit_code)
  compareString=["Multiple tar archive filenames can be specified","Print the pathname of each matching file from the archive to STDOUT",writeToFile(output)]
  returnValue=compareSting(compareString)

  if exit_code != 0:
      tet_infoline("Invalid return code"+str(exit_code))
      tet_result(TET_FAIL)
      return
  	  
  if returnValue[-1] != 0:
	tet_infoline("Verification failed ")
	tet_infoline(str(returnValue))
	tet_result(TET_FAIL)
	return
  tet_infoline("Verification successful ")	
  tet_infoline(str(returnValue))
  tet_result(TET_PASS)


def test17():
    tet_infoline("Check the /usr/bin/ptargrep --help")
    tet_infoline("Description functionality of /usr/bin/ptargrep --help")
    tet_infoline("test define 17")
    tet_infoline("/usr/bin/ptargrep --help")
    process = Popen(shlex.split("/usr/bin/ptargrep --help"), stdout=PIPE)
    output, errors = process.communicate()
    exit_code = process.wait()
    tet_infoline_output(output, exit_code)
    compareString = ["Multiple tar archive filenames can be specified",
                     "Print the pathname of each matching file from the archive to STDOUT", writeToFile(output)]
    returnValue = compareSting(compareString)

    if exit_code != 0:
        tet_infoline("Invalid return code" + str(exit_code))
        tet_result(TET_FAIL)
        return

    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return
    tet_infoline("Verification successful ")
    tet_infoline(str(returnValue))
    tet_result(TET_PASS)

def test18():
    tet_infoline("Check the /usr/bin/ptargrep --h")
    tet_infoline("Description functionality of /usr/bin/ptargrep --h")
    tet_infoline("test define 17")
    tet_infoline("/usr/bin/ptargrep --h")
    process = Popen(shlex.split("/usr/bin/ptargrep --h"), stdout=PIPE)
    output, errors = process.communicate()
    exit_code = process.wait()
    tet_infoline_output(output, exit_code)
    compareString = ["When matching files are extracted",
                     "Print the pathname of each matching file from the archive to STDOUT", writeToFile(output)]
    returnValue = compareSting(compareString)

    if exit_code != 0:
        tet_infoline("Invalid return code" + str(exit_code))
        tet_result(TET_FAIL)
        return

    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return
    tet_infoline("Verification successful ")
    tet_infoline(str(returnValue))
    tet_result(TET_PASS)

def test19():
    tet_infoline("Check the /usr/bin/ptargrep -v")
    tet_infoline("Description functionality of /usr/bin/ptargrep --v")
    tet_infoline("test define 17")
    tet_infoline("/usr/bin/ptargrep -v")
    process = Popen(shlex.split("/usr/bin/ptargrep --v"), stdout=PIPE)
    output, errors = process.communicate()
    exit_code = process.wait()
    tet_infoline_output(output, exit_code)
    compareString = ["No pattern specified",
                     "list matching filenames rather than extracting matches", writeToFile(output)]
    returnValue = compareSting(compareString)

    if exit_code != 0:
        tet_infoline("Invalid return code" + str(exit_code))
        tet_result(TET_FAIL)
        return

    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return
    tet_infoline("Verification successful ")
    tet_infoline(str(returnValue))
    tet_result(TET_PASS)

def test20():
    tet_infoline("Check the /usr/bin/ptargrep --version")
    tet_infoline("Description functionality of /usr/bin/ptargrep --version")
    tet_infoline("test define 17")
    tet_infoline("/usr/bin/ptargrep -version")
    process = Popen(shlex.split("/usr/bin/ptargrep --version"), stdout=PIPE)
    output, errors = process.communicate()
    exit_code = process.wait()
    tet_infoline_output(output, exit_code)
    compareString = ["No pattern specified",
                     "list matching filenames rather than extracting matches", writeToFile(output)]
    returnValue = compareSting(compareString)

    if exit_code != 0:
        tet_infoline("Invalid return code" + str(exit_code))
        tet_result(TET_FAIL)
        return

    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return
    tet_infoline("Verification successful ")
    tet_infoline(str(returnValue))
    tet_result(TET_PASS)


def test21():
    tet_infoline("Check the /usr/bin/ptar --help")
    tet_infoline("Description functionality of /usr/bin/ptar --help")
    tet_infoline("test define 17")
    tet_infoline("/usr/bin/ptar --help")
    process = Popen(shlex.split("/usr/bin/ptar --help"), stdout=PIPE)
    output, errors = process.communicate()
    exit_code = process.wait()
    tet_infoline_output(output, exit_code)
    compareString = ["ptar - a tar-like program written in perl",
                     "ptar is a small, tar look-alike program that uses the perl module", writeToFile(output)]
    returnValue = compareSting(compareString)

    if exit_code != 1:
        tet_infoline("Invalid return code" + str(exit_code))
        tet_result(TET_FAIL)
        return

    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return
    tet_infoline("Verification successful ")
    tet_infoline(str(returnValue))
    tet_result(TET_PASS)

testlist = {1:test1,2:test2,3:test3,4:test4,5:test5,13:test13,14:test14,15:test15,16:test16,17:test17,18:test19}
pytet_init(testlist, startup, cleanup)
