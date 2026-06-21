import os 

message = input("Enter Your Update message : ")
os.system("git add .")
os.system(f"git commit -m {message}")
os.system("git push")