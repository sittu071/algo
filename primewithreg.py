import re
def isprime(i):
    return re.compile(r'^(11+)\1+$').match('1' * i) is None

for i in range(1,100):
    if(isprime(i)):
        print(i)