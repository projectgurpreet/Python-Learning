a = 2
b = 5
biggerNum = a if a>b else b
print(f"bigger number is {biggerNum}")

a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")

username = ""
display_name = username if username else "Guest" #username if username ka mtlb ki username != ""\
print(display_name)

