def squareFunction(n):
    ''' Takes in a number n and returns its square as result'''
    print(n**2)
squareFunction(7)
print(squareFunction.__doc__)
print(squareFunction(7).__doc__)

#* docstrings ko functions, method, class or modules ko define krte huye pehle likha jata h, right after the definition of functions, method, class or modules. These are not comments.
# comments change krne se program ke output change nhi hote, but docstrings ko change krne se output change ho skte h

#squareFunction.__doc__      # docstring of the function
#squareFunction(7).__doc__   # docstring of whatever the function returns
#here the squareFunction(7) returns None, because there is no return statement in it and that's why when the .__doc__ command runs, python interpreter finds (None).__doc__ becuase of which it prints {The type of the None singleton.} in the terminal

def cubeFunction(n):
    print(n)
    ''' Takes in a number n and returns its cube as result'''
    print(n**3)
cubeFunction(7)
print(cubeFunction.__doc__) #docstring has become null now, because funciton ko define krte hi use docstring to mili hi nhi