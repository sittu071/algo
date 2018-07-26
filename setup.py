#!/usr/bin/python
import os
import commands
from ConfigParser import SafeConfigParser
import sys
#reading value from the users.cfg file

def getValueFromConfigFile(option):
    parser = SafeConfigParser()
    parser.read("users.cfg")
    value = parser.get('SEC', option)
    return value


users_list =[]
def main():
    users = getValueFromConfigFile("USER")
    soa = getValueFromConfigFile("SOA_USER")
    spa = getValueFromConfigFile("SPA_USER")
    other = getValueFromConfigFile("OTHER_USER")	
    users_list=users.split(",")
    soa_list=soa.split(",")
    spa_list=spa.split(",")
    other_list=other.split(",")
    for any in soa_list:
        users_list.append(any)
    for any in spa_list:
        users_list.append(any)
    for any in other_list:
        users_list.append(any)		

	print(users_list)
	
    ifuserexist(users_list)
    delete_soauser(users_list)
    addsoauser(soa_list)
    addspauser(spa_list)
    delete_soauser(spa_list)
    createFileset()
    print "Modifying the permission so that everyone can enter in to this directory"
    status, output = commands.getstatusoutput("/bin/chmod -R 777 ..")
    if status != 0:
        print("Failed to update permission for this test-suite folder")	
    print "Removing ^M characters from scripts , which may have caused due to editing in Windows.. "		

    status1, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../compress/ fix")
    status2, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../cp/ fix")
    status3, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../pinstall/ fix")
    status4, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../pack/ fix")
    status5, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../pax/ fix")
    status6, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../mv/ fix")
    status7, output = commands.getstatusoutput("/usr/coreutils/bin/bash ../detect_crlf.sh ../setup.env fix")
    status= status1 ^ status2 ^ status3 ^ status4 ^ status5 ^ status6 ^ status7
    if status != 0:
        print("Command:(/usr/coreutils/bin/bash ../detect_crlf.sh .. fix) failed.")
      

def ifuserexist(users_list):
    for u in users_list:
        cmd='''gtacl -s -c "safecom info user ''' +  u + ''' " ''' + ''' | grep "ERROR" '''
        print cmd
        status, output = commands.getstatusoutput(cmd)

        if status == 0:
            group_name=u.split('.')[0]
            cmd='''gtacl -s -c "safecom info group ''' +  group_name + ''' " ''' + ''' | grep "ERROR" '''
            print cmd
            status, output = commands.getstatusoutput(cmd)
            if status == 0:
                group_num=addgroup(group_name)
            else:
                cmd='''gtacl -s -c "safecom info group ''' +  group_name + ''' " ''' + ''' | grep '''
                cmd+= group_name + ''' | awk '{print $2}' '''
                print cmd
                status, group_num = commands.getstatusoutput(cmd)
                #number= int(str(group_num)[:3])
            adduser(u,group_num)

        elif u == "SUPER.SUPER":
            print("password is not altered for SUPER.SUPER")

        else:
            cmd='''gtacl -s -c "safecom alter user ''' +  u + ''',password welcome" ''' + ''' | grep "ERROR" '''
            print cmd
            status, output = commands.getstatusoutput(cmd)
            if status == 0:
                print("password altered successfully")

def adduser(user_name,number):
    print(user_name)
    STARTUID=15
    RETRYATTEMPT=10
    count=0
    while count < RETRYATTEMPT:
        user_ud= STARTUID+count

        cmd='''gtacl -s -c "safecom info user ''' + str(number) + "," + str(user_ud) + '''" | grep "NOT DEFINED" '''
        print cmd
        status, output = commands.getstatusoutput(cmd)
        if status == 0:
            cmd='''gtacl -s -c "safecom add user ''' + user_name + "," + str(number) + "," + str(user_ud)
            cmd+=''',password welcome" | grep "ERROR" '''
            print cmd
            status, output = commands.getstatusoutput(cmd)
            if status !=0:
                print("user add successfull ")
            else:
                print("useradd failed to add a user")
            break
        count+=1

def addgroup(group_name):

    number=getUnusedGroupnumber()
    cmd='''gtacl -s -c "safecom add group ''' +  group_name + ''',number ''' + str(number) + '''" | grep "ERROR" '''
    print cmd
    status, output = commands.getstatusoutput(cmd)
    if status !=0:
        return number
    else:
        print("not able to get group number and hence group add failed")

def getUnusedGroupnumber():
    GROUPNUMSTART=5
    RETRYATTEMPT=10
    count=0
    while count < RETRYATTEMPT:
        GROUPNUM=GROUPNUMSTART+count
        cmd='''gtacl -s -c "safecom info group number ''' + `GROUPNUM` + '"'' | grep "ERROR" '''
        print cmd
        status, output = commands.getstatusoutput(cmd)
        if status == 0:
            return GROUPNUM
            break
        count+=1


def addsoauser(soa_list):
    cmd='''gtacl -s -c"safecom add security-group security-oss-administrator"'''
    commands.getstatusoutput(cmd)
    for any in soa_list:
        cmd='''gtacl -s -c "safecom alter security-group security-oss-administrator,access ''' + any
        cmd+=''' * " | grep "ERROR" '''
        print(cmd)
        status, output = commands.getstatusoutput(cmd)
        if status !=0:
            print "user {} added to soa group".format(any)


def delete_soauser(soa_list):
    cmd='''gtacl -s -c "safecom add security-group security-oss-administrator "'''
    commands.getstatusoutput(cmd)
    for any in soa_list:
        cmd='''gtacl -s -c "safecom alter security-group security-oss-administrator,access ''' + any
        cmd+=''' - * " | grep "ERROR" '''
        print(cmd)
        status, output = commands.getstatusoutput(cmd)
        if status !=0:
            print "user {} deleted from soa group".format(any)





def addspauser(spa_list):
    cmd="safecom add security-group security-prv-administrator"
    commands.getstatusoutput(cmd)
    
    for any in spa_list:
        cmd='''gtacl -s -c "safecom alter security-group security-prv-administrator, access ''' + any
        cmd+=''' * " | grep "ERROR" '''
        print(cmd)
        status, output = commands.getstatusoutput(cmd)
        if status !=0:
            print "user {} added to spa group".format(any)
			
			
'''def createFileset():
    os.system('/usr/bin/python CreateFileset.py')
'''
if __name__=="__main__":main()


