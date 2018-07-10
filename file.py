import os
import string
import random

if not os.path.exists("/home/mausam/sambatest/share3"):
    os.mkdir("/home/mausam/sambatest/share3")

os.chdir("/home/mausam/sambatest/share3")

for i in range(0,25000):
    try:
        with open("share3file" + str(i) + ".txt",'w+') as file:
            var = 'mausam'.join(random.choice(string.ascii_uppercase + string.digits ) for _ in range(10))
            file.write(var)
    except:
        continue