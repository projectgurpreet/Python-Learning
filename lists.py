list1 = [1,27,3,"Gurpreet","Star",True,False,["list within list",5,8]]
# print(list1[7][2])
# if 3 in list1: #here it is checking 3 as an integer
#     print("3 is there")
# else: print("3 is not there")

# if "3" in list1: #here it is checking 3 as a string
#     print("3 is there")
# else: print("3 is not there")

# if list1[6]:
#     print("shi baat h")
# elif list1[6]==False:
#     print("false baat h")
# else:
#     print("bhaiya kuchh na mila")

# if "preet" in "Gurpreet":
#     print("Yess") #mtlb this thing works for strings too

# print(list1)
# print(list1[:])
# print(list1[0:len(list1)])
# print(list1[1:])
# print(list1[1:len(list1)])
# print(list1[:5])
# print(list1[0:5])
# print(list1[1:6])
# print(list1[1:6:2])
# print(list1[1:-5])
# print(list1[1:len(list1)-5])

#* List Comprehensions
# List = [Expression(item) for item in iterable if Condition]
#Expression: item which is being iterated
#Iterable: can be list, tuples, dictionaries, sets, arrays, strings
#Condition: if you want to apply any condition

list2 = [elem**3 for elem in list1 if type(elem)==int and len(str(elem)) ==2]
print(list2)

list3 = list1 + list2

#* gyannnn
# ⚡ extend() vs. append() vs. + OperatorIt is easy to mix these up, but they behave very differently in memory and output:Method / OperatorActionModifies In-Place?Resulting Lengthextend(iterable)Unpacks and adds all items.YesIncreases by the number of items.append(item)Adds the object as a single item.YesIncreases by exactly 1.+ OperatorCreates a brand-new combined list.NoSum of both lengths.Code Comparison Example:python# Using append puts the whole list inside the list
# list_a = [1, 2]
# list_a.append([3, 4])
# print(list_a)  # Output: [1, 2, [3, 4]]

# # Using extend merges them flat
# list_b = [1, 2]
# list_b.extend([3, 4])
# print(list_b)  # Output: [1, 2, 3, 4]
# Use code with caution.⚠️ Common PitfallsPassing a non-iterable: Trying to extend a list using an integer, float, or boolean will throw a TypeError: 'int' object is not iterable. If you need to add a single item, use append().Saving the output: Because extend() works in-place, assigning it to a variable yields None.python# WRONG
# my_list = [1, 2].extend([3, 4]) 
# print(my_list)  # Output: None
# Use code with caution.