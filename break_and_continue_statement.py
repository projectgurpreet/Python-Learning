#
#! break = "Exit the Loop".... in programming it is called "Breaking out of the loop"
#! continue = "Exit the Iteration"

from num2words import num2words #* yaha pe num2words naam ka ek module h jismein se num2words naam ka object call kra. agar sirf import num2words likhta to terko object call krne ke liye num2words.num2words(multiplier) likhna padta


multipliers = []
for multiplier in range(1,18):
    multipliers.append(num2words(multiplier)+"ja")

# Example 1

for i in range(1,18):
    if(i==7):
        break
    print("7",multipliers[i-1],7*i)
# iske andar ye code break hogaya jaise hi i == 7 true hua. iska matlab is point pe isne loop ko chhod diya. ismein ise i=7 print se pehle mila to isne use print nhi kraya
print("EXAMPLE 1 ENDED")
# Example 2

for i in range(1,18):
    print("7",multipliers[i-1],7*i)
    if(i==7):
        break
# iske andar ye code break hogaya jaise hi i == 7 true hua. iska matlab is point pe isne loop ko chhod diya. ismien ise i=7 print statement run hone ke baad mila to isne uske aage loop tod diya
print("EXAMPLE 2 ENDED")
# Example 3

for i in range(1,18):
    if(i==7):
        continue
    print("7",multipliers[i-1],7*i)
# iske andar ye code continue hogaya jaise hi i == 7 true hua. iska matlab is point pe isne i=7 milne ke baad jo bhi code run krna tha inside the loop usko chhod diya and next iteration pe chala gaya
print("EXAMPLE 3 ENDED")