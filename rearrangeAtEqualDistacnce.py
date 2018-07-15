#Algo:- Rearrange a string so that all same characters become d distance away

#Examples:- Input:  "abb", d = 2    Output: "bab"
#Input:  "aacbbc", d = 3            Output: "abcabc"
#Input: "geeksforgeeks", d = 3      Output: egkegkesfesor
#Input:  "aaa",  d = 2              Output: Cannot be rearranged

str = "geeksforgeeks"   #Predefined string/hardcorrded string
bin_list = [0] * 256    #list with 256 length, initialize with zero
empty_dictionary = {}   #An empty dictionary
lengthofdict = 0        #initialise length of dictionary as zero
lengthofstr = len(str)  #declare the length of string

for char in str:     #this loop is used for count number of occurence of every character
    if bin_list[ord(char)] == 0:    #check the ascii value of charcter containing zero or not
        bin_list[ord(char)] = 1     #if ascii value contain zero then replace it with one
        empty_dictionary.update({char:1})   #update the dictionary with value 1
        lengthofdict = lengthofdict + 1     #increses the counter of length
    else:
        bin_list[ord(char)] = bin_list[ord(char)] + 1    #increase the count inside the ascii value
        value = empty_dictionary[char]                   #keys value stored in a variable value
        value = value + 1                                #increase value by 1
        empty_dictionary.update({char:value})            #update the dictionary with newly occurnce character

bin_list = sorted(bin_list,reverse=True)                 #sorted the list in descending order
bin_list = bin_list[0:lengthofdict]                      #removed the list which contains zero value
rearrangelist = [0] * 13                                 #declared a new list
count = 0                                                #initialise a counter
mantainDistance = lengthofstr //  bin_list[0]            #keep the distance between each character

for key in empty_dictionary:                             #Rearranged all string with equal distance between same character
    valueofkey = empty_dictionary[key]
    temp = count
    while valueofkey != 0:
        if rearrangelist[temp] == 0:
            rearrangelist[temp] = key
            temp = temp + mantainDistance
            valueofkey = valueofkey - 1
        else:
            count = count + 1
            temp = count
    count = count + 1


print(''.join(rearrangelist))                                    #printed the rearranged list output:   gekgeksefseor