def rev(string):
    if string == "":
        return string
    else:
        return rev(string[1:]) + string[0]

def rearrangestring(result):
    count = 0
    for i in result:
        length = len(i)
        for j in range(0,length//2):
            i = list(i)
            i[j],i[length - j -1] = i[length - j -1],i[j]
        i = ''.join(i)
        result[count] = i
        count = count + 1
    return result

string = "i love programmnig very much"
result = rev(string)
result = result.split()
result = rearrangestring(result)
result = ' '.join(result)
print(result)