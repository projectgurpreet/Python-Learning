# #* f-strings allow us to put variables into strings

name = "Gurpreet"
age = 17

print(f"My name is {name} and i am {age} years old")

price = 270.2727

print(f"THe price of these apples is {price:.2f}")
print(f"THe price of these apples is {price:.3f}")
print(f"THe price of these apples is {price:.1f}")
print(f"THe price of these apples is {price}")
print(f"THe price of these apples is {price:.0f}")
#print(f"THe price of these apples is {price:.-1f}") #* senseless

print(type(f"{2*30}")) #* after all it is a string

print(f"{2*30}")

print(f"This is what I made using f-strings: {{2*30}}") #* double curly braces will make these brackets appear as they are and no value will be populated into them

