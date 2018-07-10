import  string
a     = [5, 2, 4, 3, 6, 1]
alist = [5, 2, 4, 3, 6, 1]
#a.append("GeeksforGeeks")
#a.append("GeeksQuiz")
#a.append("CLanguage")

length = a.__len__()
length = length - 1
def bubblesort(length):
    for i in range(0,length):
        for j in range(0,length):
            if a[j] > a[j+1]:
                c = a[j]
                a[j]=a[j+1]
                a[j+1] = c


def selectionsort(length):
    for i in range(0,length):
         for j in range(i,length):
            if a[i] > a[j+1]:
                c = a[i]
                a[i] = a[j+1]
                a[j+1] = c


def insertionsort(length):
        for i in range(1,length+1):
            value = a[i]
            hole = i
            while(hole > 0 and a[hole -1] > value):
                a[hole] = a[hole -1]
                hole = hole -1
            a[hole] = value


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",alist)


def partion(a,low,high):
    i = (low -1)
    pivot = a[high]
    for j in range(low,high):
        if a[j] <= pivot:
            a[i],a[j] = a[j],a[i]
    a[i + 1],a[j + 1]= a[j + 1],a[i + 1]

    return (i + 1)

def quicksort(a,low,high):
    if low < high:
        pi = partion(a,low,high)
    quicksort(a,low,pi -1)
    quicksort(a,pi + 1,high)

#bubblesort(length)
#print(a)
#selectionsort(length)
#print(a)
#insertionsort(length)
#print(a)
#mergeSort(alist)
#print(alist)

length = len(a)
low=0
length = length - 1
quicksort(a,low,length)
print(alist)