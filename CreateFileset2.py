__author__ = 'Mausam'

import commands
import os
import time

dir1 = "/fileset2"
fileset2 = "dir1"


def createFilesetVersion2(fileset, mount):
    cmd = '''gtacl -c "scf assume \$ZPMON; add fileset ''' + fileset + ''',pool rootpool,catalog \$oss,MNTPOINT \\\"''' + mount + '''\\\" "'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)
    stopFileset(fileset)
    startFileset(fileset)
    cmd1 = '''gtacl -c "scf assume \$ZPMON;status fileset ''' +fileset+''',det" | grep "CatalogVersion"'''
    print(cmd1)
    output = commands.getstatusoutput(cmd1)
    print(output)
    stopFileset(fileset)
    time.sleep(10)
    if (output[1] == " CatalogVersion......... 4    "):
        downgradeFileset(fileset)

    startFileset(fileset)
    cmd1 = '''gtacl -c "scf assume \$ZPMON;status fileset '''+fileset+''',det" | grep "CatalogVersion"'''


    print(cmd1)
    output = commands.getstatusoutput(cmd1)
    print(output)
    stopFileset(fileset)
    time.sleep(10)
    if (output[1] == " CatalogVersion......... 3    "):
        downgradeFileset(fileset)

    startFileset(fileset)


def startFileset(fileset):
    print("starting the fileset", fileset, "after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;start fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def stopFileset(fileset):
    print("stoping the fileset", fileset, "after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;stop fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def downgradeFileset(fileset):
    print("downgrading  the fileset", fileset, "after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;diagnose fileset ''' + fileset + ''',downgrade''' '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def deleteFileset(fileset):
    print("stoping the fileset", fileset, "after newly creation")
    cmd = '''gtacl -c "scf;assume \$zpmon;delete fileset ''' + fileset + '''"'''
    print(cmd)
    output = commands.getstatusoutput(cmd)
    print(output)


def main():
    # creating two directory

    if not os.path.exists(fileset2):
        os.mkdir(fileset2, 777)


cmd = "chmod 777 " + dir1
print(cmd)
commands.getstatusoutput(cmd)
createFilesetVersion2(fileset2, dir1)

if __name__ == "__main__": main()
