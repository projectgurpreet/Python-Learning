# num = 9
# print(num)

# def hello():
#     num = 7

#     print(num)
#     print(f"local num is {num}")
#     print("hello world")

# print(f"global num is {num}")
# hello()
# num = 7
# print(f"global num is {num}")

# local variable function mein bnta h and function ke andar hi accessible hota h
# global variable function ke bahar bnta h and andar bhi access ho skta h


x=10

def fanksan():
    # x=5
    global x
    x= 4 #now global variable x ko use krega ye
    y=4
    print(x,y)

fanksan()
print(x)
try: print(y)
except: print("i told you y is a local variable")
