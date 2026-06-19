# 
#* while loop with else
i=8
while(i<=7):
    print(i)
    i = i+1
else:
    print("loop over hogaya and ab python interpreter while loop se bahar aagaya h")

#* do while loop emulation in python, given that a native do while loop doesn't exist in python

num = 0
while True: 
    num = num +1
    print(num)
    if(num%100==0):
        break