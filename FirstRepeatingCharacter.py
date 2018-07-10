str = "Geeksforgeeks"
str=str.lower()
lt=list(str)
length = len(lt)

for i in range(0,length):
    flag = 0
    for j in range(i+1,length):
        if lt[i] == lt[j]:
            flag = 1
    if flag == 0:
        print(lt[i])	
        break