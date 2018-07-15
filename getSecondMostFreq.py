#Program to find second most frequent character

#Algo :- Given a string, find the second most frequent character in it. Expected time complexity is O(n) where n is the length of the input string
    #input str = "aabababa" -> output: Second most frequent character is 'b'
    #input str = "geeksforgeeks" -> Output: Second most frequent character is 'g'
    #input str = "geeksquiz" -> Output: Second most frequent character is 'g'


str = "geeksforgeeks"  #Predefined string/hardcorrded string
bin_list = [0] * 256    #list with 256 length, initialize with zero
empty_dictionary = {}   #An empty dictionary
length = 0

for char in str:         #this loop is used for count number of occurence of every character
    if bin_list[ord(char)] == 0: #check the ascii value of charcter containing zero or not
        bin_list[ord(char)] = 1  #if ascii value contain zero then replace it with one
        empty_dictionary.update({char:1}) #update the dictionary with value 1
        length = length + 1 #increses the counter of length
    else:
        bin_list[ord(char)] = bin_list[ord(char)]  + 1  #increase the count inside the ascii value
        value = empty_dictionary[char]                  #keys value stored in a variable value
        value = value + 1                               #increase value by 1
        empty_dictionary.update({char:value})           #update the dictionary with newly occurnce character

sorted_list = sorted(bin_list,reverse=True)             #sorted the list in descending chracter
sorted_list = sorted_list[0:length]                     #removed the list which contains zero value

for index in range(0,length):                           #second highest value in list
    if sorted_list[index] > sorted_list[index +1]:
        value = sorted_list[index + 1]
        break

for key in empty_dictionary:                            #find the key corresponding to the value
    if empty_dictionary[key] == value:
        print("Second most frequent char is ",key)      #print the second most frequent character
        break




