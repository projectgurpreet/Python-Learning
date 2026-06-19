# tup1 = (1) #python confuse hogya integer h ya tuple
# print(type(tup1))

# tup2 = (1,) #ab ye tuple hi h
# print(type(tup2))

# tup3 = (1,"sdaihdjks") #ab ye tuple hi h
# print(type(tup3))

# tup = ("alpha","beeta","mama",1,2,3,True,False)
# if "mama" in tup:
#     print("mama is there")

# #tuples are unchangeable so slicing pe naya tuple return hota h old tuple change nhi hota

# tupla = tup[1:6:2]
# print(tupla)

# tupli = ("ek","do","teen","chaar","eka","paanch","ek","chhe","saat","ek","aath","noo","das")
# print(len(tupli))
# print(tupli[1:8])
# print(tupli.count("ek"))
# print(tupli.index("chaar"))
# print(tupli.index("ek"))
# print(tupli.index("ek",1,8))
# listli = list(tupli)
# eka_ka_index = listli.index("eka")
# listli.pop(eka_ka_index)
# listli.insert(eka_ka_index,"ek")
# print(listli)
# tupli = tuple(listli)
# print(tupli)
# #how did the tuple change man!!! 
# # it didn't change the original tuple, you just overwrote the original data under the name "tupli". now that variable named tupli has a different value

tuplo = (1,"one",True,[1],(1),(1,))
tuplo[tuplo.index([1])].append(2)
print(tuplo)
# so basically you did't change the tuple, you changed the element inside of it, which was a list. but changing an element won't change it?