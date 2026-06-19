import time
print(time.gmtime(0)) #gives the epoch time
print(time.time()) #gives the time in seconds since epoch 
currentTime = time.ctime(time.time()) #converts the seconds time from epoch into a string in local time
print(currentTime)
#Delaying time in loops #!will be checked after learning loops

#*time.struct_time
#ye ek class h jiske andar multiple functiions and ham in functions ka use dekhne wale h
localtime = time.localtime(time.time())
print(localtime) #ye localtime wala function ek specified timestamp jo iski parenthesis mein dena hota h (custom bhi de skte h merko current time ke liye chahiye tha isliye maine time.time() ka use kiya)
time_sec = time.mktime(localtime)
print(time_sec) # mktime is just the inverse of localtime, struc_time class object ko change krke seconds banadega since epoch









#* https://www.geeksforgeeks.org/python/python-time-module/
#* this is the link for time module