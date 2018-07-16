#algo: Enter a number through the keyboard and find the number

#example num=4 output:24

def fact(num):  #function defined to find factorial of a number
    if num == 1:
        return 1
    else:
        return fact(num - 1) * num



num = int(input())  #enter a number through a keyboard
res = fact(num)  #function called
print(res)       #result of factiora get printed