num = input("Give a number: ")
print(f"Multiplication Table of {num} is given as follows:-")

#! very very important thing, vaha use kr jaha error aane ki sambhaavna h. yaha agar user ne input mein integer nhi diya to for loop nhi chalega isliye hamne use try kiya and except mein jo "Exception" h vo error h to use "e" naam ke variable mein store krdiya, agar vo error ke variable ko use krne ka man nhi h to Exception as e likhen ki need nhi h bas seedha except likh ke bhi kaam chal jayega
try:
  for i in range(1,8):
    print(f"{int(num)} times {i} = {int(num)*i}")
except Exception as e:
  print(f"sorry an error came which was {e}")    

print("end of code")



#!#!#!#!#!#!#!#!#!##!#!#!#!#!#!# VVVVVVVVIMPORTANT

