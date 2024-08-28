# Name: Logan Bond
# Class: 6th Hour
# Assignment: HW3

#Print Hello World!

#Create a list with 5 strings containing 5 different names in it
#Append a new name onto the Name List
#Print out the 4th name on the list

#Create a list with 4 different integers in it
#Insert a new integer into the 2nd spot
#Print the Integer List
#Sort the list from lowest to highest
#Add the 1st three numbers on the sorted list together
#Print the sum




print("Hello World!")

list_o_names = ["Sir Jeremy Pattytown the 378th","Logan Bond","Engineer TF2","Coach Mack","Stanley"]
print(list_o_names)
list_o_names.append("Kyle")
print(list_o_names)
print(list_o_names[4])

numlist = [7,6127,4,55]
print(numlist)
numlist.insert(1, 427)
print(numlist)
numlist.sort()
print(numlist)
sum = numlist[0] + numlist[1] + numlist[2]
print(sum)