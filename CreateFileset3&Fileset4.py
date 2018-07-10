__author__ = 'Mausam'

import commands
import os
import time

dir1="/fileset4"
dir2="/fileset3"
fileset3="fileset3"
fileset4="fileset4"

def createFilesetVersion3(fileset, mount):
    cmd = '''gtacl -c "scf assume \$ZPMON; add fileset ''' + fileset + ''',pool rootpool,catalog \$oss,MNTPOINT \\\"''' + mount + '''\\\" "'''
   # cmd += ''',mntpoint \\"''' + mount + ''' \\"" '''
    print(cmd)
    output=commands.getstatusoutput(cmd)
    print(output)
    stopFileset(fileset)
    startFileset(fileset)
    cmd1 = '''gtacl -c "scf assume \$ZPMON;status fileset fileset3,det" | grep "CatalogVersion"'''
    print(cmd1)
    output = commands.getstatusoutput(cmd1)
    print(output)
    stopFileset(fileset)
    time.sleep(10)
    if (output[1] == " CatalogVersion......... 4    "):
        downgradeFileset(fileset)

    startFileset(fileset)

def createFilesetVersion4(fileset, mount):
    cmd = '''gtacl -c "scf assume \$ZPMON; add fileset ''' + fileset + ''',pool rootpool,catalog \$oss,MNTPOINT \\\"''' + mount + '''\\\" "'''
   # cmd += ''',mntpoint \\"''' + mount + ''' \\"" '''
    print(cmd)
    output=commands.getstatusoutput(cmd)
    print(output)
    stopFileset(fileset)
    startFileset(fileset)


def startFileset(fileset):
    print("starting the fileset",fileset,"after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;start fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def stopFileset(fileset):
    print("stoping the fileset",fileset,"after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;stop fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def downgradeFileset(fileset):
    print("downgrading  the fileset",fileset,"after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;diagnose fileset ''' + fileset + ''',downgrade''' '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)
def deleteFileset(fileset):
    print("stoping the fileset",fileset,"after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;delete fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def main():
#creating two directory

    if not os.path.exists(dir1):
        os.mkdir(dir1,777)
    if not  os.path.exists(dir2):
        os.mkdir(dir2,777)
cmd="chmod 777 "+ dir1
print(cmd)
commands.getstatusoutput(cmd)
createFilesetVersion3(fileset3,dir2)
cmd="chmod 777 "+ dir2
print(cmd)
commands.getstatusoutput(cmd)
createFilesetVersion4(fileset4,dir1)
#deleteFileset(fileset3)
#deleteFileset(fileset4)


if __name__ == "__main__": main()
