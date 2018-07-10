def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r,m):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            print(a[l],a[i])
            permute(a, l + 1, r,print("Recursion called"))
            a[l], a[i] = a[i], a[l]  # backtrack
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1,m=0)