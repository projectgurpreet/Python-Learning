import time
timestamp = time.strftime("%H:%M:S")
# print(timestamp)
hour = int(time.strftime("%H"))
# print(hour)
minutes = int(time.strftime("%M"))
# print(minutes)
seconds = int(time.strftime("%S"))
# print(seconds)

if(0<=hour<=11 and 0<=minutes<=59 and 0<=seconds<=59):
    print("Good Morning Star 🌄")
elif(12<=hour<=16 and 0<=minutes<=59 and 0<=seconds<=59):
    print("Good Afternoon Star ☀️")
else:
    print("Good Evening Star 🌆")