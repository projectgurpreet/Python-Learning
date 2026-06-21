# # num = input("Give a number: ")
# # print(f"Multiplication Table of {num} is given as follows:-")

# # #! very very important thing, vaha use kr jaha error aane ki sambhaavna h. yaha agar user ne input mein integer nhi diya to for loop nhi chalega isliye hamne use try kiya and except mein jo "Exception" h vo error h to use "e" naam ke variable mein store krdiya, agar vo error ke variable ko use krne ka man nhi h to Exception as e likhen ki need nhi h bas seedha except likh ke bhi kaam chal jayega
# # try:
# #   for i in range(1,8):
# #     print(f"{int(num)} times {i} = {int(num)*i}")
# # except Exception as e:
# #   print(f"sorry an error came which was {e}")    

# # print("end of code")

# #until now i hadn't learnt about exception types, raise, finally. now i have a quick quiz from the course 

# a = input("Enter a number between 5 and 9: ")

# class customError (Exception):
#     # print(f"error was found and it was {Exception}")  
#     pass

# try: 
#     int(type(a))==str
#     # if a=="quit":
#     #      print("program quit")
#     print("string")
# except: 
#     print("not string")



#! relearning exception handling
#quick quiz trying 
a = input("Enter a number between 5 and 9: ")

try:
    if a == "quit": 
        print("Mission Abort")
except:
    int(a)
    try:
        if 5<=int(a)<=9:
            print(f"the integer was {int(a)}")
        else:
            print(f"the integer was not between the asked range. your given integer was {int(a)}")
    except:
        print("a valid entry was not made.")
finally:
    print("Cycle ended")