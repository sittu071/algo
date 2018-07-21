def findFirstNonRepeating(list):
    bin_list = [0] * 256
    dic = {}
    for index in list:
        if bin_list[ord(index)] == 0:
            dic[index] = 1
            bin_list[ord(index)] = 1
        else:
            if bin_list[ord(index)] >=2:
                pass
            else:
                dic.pop(index)
                bin_list[ord(index)] = bin_list[ord(index)] + 1

    for key in dic:
        print("First non-repeating character so far is",key)
        break

str = input()
list = list(str)
findFirstNonRepeating(list)