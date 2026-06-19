# random = {"ek",1,"ven",True,1,1,1,1,1,1,1,True,True}
# random = {1,True}
# random = {} #ye ek empty set nhi ek empty dictionary h
# tinuninu = set() #aise banate h ek empty set
# print(type(random))
# print(random)
# print(type(tinuninu))
# print(tinuninu)

# cars = {"audi","mercedes","pagani","bmw","rollsroyce","bugatti","lamborghini","ferrari","koenigsegg","bugatti","mercedes"}
# print(cars) #order maintain hone ki koi guarantee nhi hoti set mein, and multiple chezeen likhne ka bhikoi mtlb nhi hota ismein
# # to access values inside a set:
# for car in cars:
#     print(car) #order maintain hone ki koi guarantee nhi h

# cities1 = {"kalchhetar","khethal","karnal","delhi","pehowa"}
# cities2 = {"pehowa","delhi","madrid","hisar"}

# cities3 = cities1.union(cities2)
# print(cities3)
# cities4 = cities2.union(cities1)
# print(cities4)

# cities5 = cities1.intersection(cities2)
# print(cities5)
# cities6 = cities2.intersection(cities1)
# print(cities6)
# print(cities1,cities2,cities1.union(cities2))
# cities1.update(cities2) #cities1 mein hi cities2 wali vo cheezen daaldi jo cities1 mein nhi h. union wale se indivdual sets same rhe, ab yaha pe cities1 wala set hi change hogaya
# print(cities1,cities2,cities1.union(cities2))

#isi way mein intersection se khelte h

s1 = {1,2,3,1,5,7,3}
s2 = {2,4,2,5,9,8}

# print(s1,s2,s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1,s2)

# print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference_update(s2))
# print(s1)
# print(s1.difference(s2))
# print(s2)
# print(s2.difference(s1))    
# s1.difference_update(s2)

# print(s1)


# print(s2.difference(s1))

# a1 = {1,2,3}
# a2 = {4,5,6}
# a3 = {2,5,7}
# print(s1.isdisjoint(s2))
# print(a1.isdisjoint(a2))
# print(a1.isdisjoint(a1))
# print(a1.isdisjoint(a3))
# print(a1.intersection(a2))

