import os
import timeit
import time

print("Write operation into tht mount " + os.environ['MNT'] + "")
print("Eneter the source file locattion " + os.environ['SRC'] + "")
var = 1024
for cre in [1, 10, 50, 100, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000,
            8500, 9000, 9500]:
    var = cre*1024
    with open(os.environ['SRC'] + '\\file' + str(cre) + 'KB', 'w') as f:
        f.seek(var -1)
        #f.write('cabc' * cre)
        f.write("\0")

sizes = ["10", "20"]
for size in sizes:
    start = time.time()
    end = time.time()
    print("Copy file " + str(size) + " from the source [" + os.environ['SRC'] + "] to mount " + os.environ[
        'MNT'] + " Time " + str(end - start))
