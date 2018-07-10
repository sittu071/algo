def partition(li,slice,l,n):
    if l == n:
       toString(li[:])
    else:
        toString(li[:slice])
        partition(li[slice:],slice,l+1,n)


str="Mausam_kumar_Sinha"
li=list(str)
length= len(li)
n =3
l=1
slice=length//n #6
slice = slice
partition(li,slice,l,n)