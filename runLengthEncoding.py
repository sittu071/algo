string = "wwwwaaadexxxxxx"
li = list(string)
dic = {}
bin_arr = [0] * 128
for i in li:
    if bin_arr[ord(i)] == 0:
       dic[i] = 1
       bin_arr[ord(i)] = 1
    else:
        val = dic[i]
        dic[i] = val + 1
res = ""
for i in dic:
    res = res + i + str(dic[i])
print(res)