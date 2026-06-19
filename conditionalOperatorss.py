# Conditional Operators
# >,<,<=,>=,!=,==

# ! if-else

# age = int(input("Enter Your Age: "))
# if(age>18):
#     print("You can vote")
#     print("yesss")
# else:
#     print("chal be tu vote ni krega")
#     print("nah dude")
# print("ye to hoga hi and btw teri age",age,"h")

# ! if else el-if
# * ismein pehle "if" ko check krega fir "elif" ko fir agle "elif" ko and so on jab tak vo "else" pe na pohonch jaye. also jis stage pe jaake condition true aajegi vhi pe code stop hojega and vo part execute hojega, uske aage ke elif ya else ni work krenge

# budget = int(input("Enter your budget: "))
# applePrice = int(input("What's the apple price today? : "))
# mangoPrice = int(input("What's the mango price today? : "))

# if(budget >= applePrice + mangoPrice):
#     print("You can afford both simultaneously")
# elif(budget >= applePrice and budget >= mangoPrice):
#     print("You can afford both individually")
# elif(budget>=applePrice and budget<mangoPrice):
#     print("You can only afford apples")
# elif(budget<applePrice and budget>=mangoPrice):
#     print("You can only afford mangoes")
# else:
#     print("Sorry, you can't afford any")

#! nested if statements
#* ismein ek if elif else ladder ke andar multiple if elif else ladders introduce kri jati h, example is given

# list1 = {1,2,3,4,5,6,7,8,9,10}
# list2 = {11,12,13,14,15,16,17,18,19,20}
# num = int(input("Enter A Number: "))
# if(num<0):
#     print("number is negative and its value is", num)
# elif(num>0):
#         if(num<=10):
#             print("number belongs to the interval",list1,"and its value is",num)
#         elif(num>10 and num<=20):
#             print("number belongs to the interval",list2, "and its value is",num)
#         else: print("number is greater than 20","and its value is",num)
# else: print("number is 0")
