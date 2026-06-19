# from num2words import num2words

# #* required Input Function
# def get_required_input(promptMessage):
#   while True:
#     givenInput = input(promptMessage).strip()
#     if givenInput:
#         return givenInput
#     else: print("It is required!! Plz Put in the Value")

# #* total num list as ordinals
# totalNum = int(input("How Many Numbers Do You Want To Enter? : "))
# totalNumListOrdinals = []
# for numListCount in range(1,totalNum+1):
#     totalNumListOrdinals.append(num2words(numListCount, to="ordinal"))
# # print(totalNumListOrdinals)

# #* getting numbers in a list from user
# numList = []
# for i in range(totalNum):
#     newNum = get_required_input("Enter your " + totalNumListOrdinals[i] + " number: ")
#     numList.append(newNum)
# # print(numList)

# #* Arithmetic Mean Calculation Formula

# def calculateArithmeticMean():
#     totalSum = 0
#     for i in range(totalNum):
#         totalSum = totalSum + int(numList[i])
#     arithmeticMean = totalSum/totalNum
#     print(arithmeticMean)

# calculateArithmeticMean()

#* Function Arguements
# def average(a=2,b=1):
#    print("The Average Is",(a+b)/2)
#    print("a=",a)
#    print("b=",b)
# average()
# average(2,4)
# average(4,2)
# average(a=2,b=4)
# average(b=4,a=2)
# average(b=4)
# average(5)

# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum + i
#     print("Average =",sum/len(numbers))
# average(2,5,3,6,5)

def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return 7 
   #  return sum/len(numbers) #* return mtlb vapas chale jao ye value leke and aage mat badho
c= average(2,5,3,6,5)
print(c)
