import string
#reverse a string
def reverse(str):
    if len(str)<=1:
        return str
    return reverse(str[1:]) + str[0]

str=input()#input a string
str=reverse(str)#reverse input string
str=str.split(' ')#split with comma after reverse a string
count=0
str_list=[]#append string in list

for i in str:
    str2=reverse(str[count])
    str_list.append(str2)
    count=count+1
str_list=' '.join(str_list)#finally remove all comma and join string
print(str_list)