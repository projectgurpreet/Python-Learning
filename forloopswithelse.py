for i in range(5):
    print(i)
else: print("i ni mila")

for i in []:
    print(i)
else: print("i ni mila")

for i in range(7):
    print(i)
    if(i==5): break
else: print("i ni mila") #ismein else ni work hua because loop successfully over nhi hua, instead break hogaya, loop hi exit hogaya

for i in range(7):
    if(i==5): continue
    print(i)
else: print("i ni mila")