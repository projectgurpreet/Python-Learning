# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1) #same function ko usi ke andar call krdiya mtlb recursion

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))
# print(factorial(7))

# def factorial(n):
#     if (n==0):
#         return 1
#     else: 
#         return n*factorial(n-1)
# print(factorial(1)) #both of these work

#but what if....
# def factor(n):
#     return factorial(n) #! bhai factorial naam ka koi direct function ni hota 😃🤣

# print(factor(0))
# print(factor(1))
# print(factor(5))

#recursion questions ke maje lete h ab jee mains ke
#Question: a1 = 1 and an+1 = an + 2n. find a7...... Answer:43
# def recursionKushan1(n):
#     if n==1:
#         return 1
#     else:
#         return recursionKushan1(n-1) + 2*(n-1)
# print(recursionKushan1(7))    


# def fibonacciSeries(n):
#     if (n==0):
#         return 0
#     elif (n==1):
#         return 1 
#     else: 
#         return fibonacciSeries(n-1) + fibonacciSeries(n-2)
# print(fibonacciSeries(7))

# for i in range(8):
#     print(f"Fibonacci series mein value dekhe to F{i} = {fibonacciSeries(i)}")