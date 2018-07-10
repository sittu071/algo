str = "Mausam kumar sinha is a great guy i know him when he was just a four year old, a beautiful face with beautiful eye "
length = len(str)
arr = []
count = 0
empty={}
for i in range(0,length):
    for j in range(1,length):
        if str[i] == str[j] and str[i] != ' ':
            count = count + 1
            empty.update({str[i]:count})
    count = 0

for k in empty.values():
    arr.append(k)

arr.sort()
length = len(arr)


for i in empty.keys():
    if arr[length -1] == empty.get(i):
        print(" Max occurring character is ",i)