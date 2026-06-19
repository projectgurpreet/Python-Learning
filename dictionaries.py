# dict = {"name" : "Gurpreet", "age":17,"eligible for vote":False} #jo colon se pehle likhi h vo keys h and jo colon ke baad likhi h vo unki corresponding values h
# # print(dict["name"]) #agar name ki jagah name2 likhduin to ye error throw krdega
# # print(dict.get("name")) #agar name ki jagah name2 likhduin to ye None dedega

# # print(dict.keys())
# # print(type(dict.keys())) #dict_keys and dict_values alag datatypes h apne aap mein
# # print(dict.values())

# # for key in dict.keys():
# #     print(f"The value corresponding to the key {key} is {dict[key]}")

# # print(dict.items())
# # print(type(dict.items())) #ye bhi separate data type h, but ye as a tuple return krta h values ko

# for key,value in dict.items():
#     print(f"The value corresponding to the key '{key}' is '{value}'")

# # for value,key in dict.items():
# #     print(f"The value corresponding to the key '{key}' is '{value}'") #* iska matlab a,b as a tuple lega ye and usko correspondingly ordered way mein hi cheezen assign krega, mtlb first variable a ko keys dega and second variable b ko values dega

# for key,key in dict.items():
#     print(f"The value corresponding to the key '{key}' is '{key}'") #* pehle key ko actual key mili and dusri key ko actual value mili to key naam ka variable overwrite hogaya and key naam ke variable mein finally values store hogayi
#     print(f"The value corresponding to the key '{key}' is '{value}'") #* refer to awesomegyan.py

info = {"name":"Gurpreet", "age":17,"eligible":True}
# print(info)
# info.update({"name":"alpha"})
# print(info)
# info.update({"DOB":"27/01/2009"})
# dob = {"DOB":"27/01/2009"}
# info.update(dob) isse bhi same hi result milta. overall ek dictionary deni hoti h purani dictionary ko update krne ke liye. agar koi key pehle se hogi to uski value change krdega. and if no, then new key value pair bana dega
# print(info)

# info.clear() #empty dictionary banadega
# print(info)

# info.pop("eligible") #ek particular key hata deta h
# print(info)

# print(info.popitem()) #jo item pop kri h use as a tuple return kra h (key,value) is form mein
# info.popitem() #last key value pair hata deta h
# print(info)

# del info #puri dictionary delete krdi
# print(info) #error dega
# del info["age"] #sirf is key ko delete krega
# print(info)

# del info["hello"] #error dega since use ye key hi ni mili
# print(info)

