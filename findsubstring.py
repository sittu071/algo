import re

count = 97
li = [0] * 256
def isprime(n):
    return re.compile(r'^(11+)\1+$').match('1' * n) is None

for x in range(3,300):
    if isprime(x):
        if count != 123:
            li[count] = x
            count = count + 1
        else:
            break
#print(li[97:123])

string = "sun"
substring = list(string)
substringvalue = 1
for i in substring:
    val = ord(i)
    substringvalue = substringvalue * val


list = ["geeksforgeeks", "unsorted", "sunday", "just", "sss"]

for i in list:
    strval = 1
    for j in i:
        val = ord(j)
        strval = strval * val
    if strval%substringvalue == 0:
        print(i," is the substring of ",string)