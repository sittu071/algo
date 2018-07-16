#Algo: input a number and find the fibonacci term of that number

def fibo(n,a,b): #function called
    if n > 0:
        print(a+b,end=" ")
        fibo(n -1,b,a + b)

in_num = int(input()) #input a number
firstNumber = 0   #first Number initialise with zero
secondNumber = 1  #second number initialise with one
print(firstNumber,secondNumber,end=" ") #print the first and second number
fibo(in_num,firstNumber,secondNumber) #function called