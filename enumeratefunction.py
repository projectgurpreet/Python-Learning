cities = ["Tokyo", "Paris", "New York", "London", "Mumbai"]

for index,city in enumerate(cities):
    print(index,city)

for index,city in enumerate(cities,start=1): #isse index mein jo values store hongi vo 1 se start hongi
    print(index,city)
for city_tuple in enumerate(cities):
    print(city_tuple) #do variables diye the to ye tuple unpack hogaya

city_name = "Kalachhetar" 
for serial_num,letter in enumerate(city_name, start=1):
    print(f"the letter at position number {serial_num} is {letter}")

cities = ("Tokyo", "Paris", "New York", "London", "Mumbai")
for index,city in enumerate(cities):
    print(index,city)
