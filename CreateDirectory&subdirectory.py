#the written test case will create 10 directory,inside each directory it will create 1023 subdirectory recursively
import os
import commands
import shutil

pppath="/temp/mausam/recurtest"
path="/temp/mausam/recurtest/t"


if not os.path.exists("/temp/mausam/recurtest"):
    os.mkdir("/temp/mausam/recurtest")

#from here subdirectory will create subdirectory

for i in range(1,11):
        if not os.path.exists(path + str(i)):
            os.mkdir(path + str(i))
        os.chdir(path + str(i))
        print(path + str(i))
        for j in range(1,1024):
            if not os.path.exists('d' + str(j)):
                os.mkdir('d' + str(j))
            os.chdir('d' + str(j))
        os.chdir(pppath)

