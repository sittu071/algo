
s = "ABC"
def display(a,n):
    flag = 0
    for i in range(0,n+1):
        if a[i] == 1:
            print(s[i],end="")
            flag = 1
    if flag == 0:
        print("null set")
    print("\n",end="")

def substring(a,k,n):
    if k == n:
        a[k] = 0
        display(a,n)
        a[k] = 1
        display(a,n)
    else:
        a[k] = 0
        substring(a,k + 1,n)
        a[k] = 1
        substring(a,k + 1,n)

length = len(s)
li = [0] * length
m = 0
substring(li,m,length -1)