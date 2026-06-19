for a, b in [("x", 1), ("y", 2)]:
    pass

print(a)
print(b) #* ab yaha pe loop to pass pe h mtlb hamein ismein baadmein kaam krna tha, lekin loop ne kya kra jab values assign kri to initially a ko x and b ko 1 diya, fir vo aage move hua a ko y and b ko 2 diya, but uske baad kuchh ni kra. and ye 2 variables a and b mein values store hoke rehgyi, jo outside the loop bhi access kri ja skti h


#The loop finishes, and the variables remain available.

#So the rule is:

#In Python, for, if, while, and try blocks do not create a new scope. Variables created inside them are accessible outside the block. Only things like functions, classes, and modules create their own scopes.

#example
def func(num):
    x=num
    print(x) #ye error nhi dega because x and print command both are within the function
func(2)

#print(x) #ye error dega because x is within the funciton