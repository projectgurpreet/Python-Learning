# Coding:
# If the word contains at least 3 characters:
#   - Remove the first letter and append it at the end
#   - Append three random characters at the beginning and at the end
#
# Else:
#   - Simply reverse the string


# Decoding:
# If the word contains less than 3 characters:
#   - Reverse it
#
# Else:
#   - Remove 3 random characters from the start and end
#   - Remove the last letter and append it to the beginning

# plan: So first of all, I think I should do it like this:
#1. I should build the coding part only, and then just keep reversing the steps for the decoding part.
#2. I'm thinking of doing it like two functions which ask the user to pick whether they want coding or decoding.
#3. If the user types something else, then it raises an error.
#I have got a plan. I can do this. For example, I can ask, "What do you want, code or decode?" and then check the code versus decode thing. If none of these two strings is chosen, then there is an error thrown at it. For example, if the user says code, then the coding function, the function named coding, is called. Inside that function I can ask for an input, and then that input will be obviously a string. After that I will save a variable as the length of the input, which will be the length of it. Then I can apply the rules. If the length is less than three, then I can do one thing: just reverse it. For reversing, I would like to turn it into a list, then use that list.reverse() function, then again turn that list into a string, and then save it. This would work. If the length is greater than or equal to three, what I will do is:
# 1. Turn it into a list
# 2. Save the zeroth index in a separate variable and then append that to the last
# 3. Pop it from the first
# 4. Have a list or tuple so that it cannot be mutated with all the 26 letters in it
# 5. Choose any of the letters at random
# 6. Put three of those random letters at first
# We can have a separate function for this named "random variable picker" or "random letter picker", which would add three letters in the start and three letters in the end using a for loop or a while loop. I would say.And then we can just convert that list into a string again. Now I am going to keep it to Just displaying the coded and the decoded thing from the input. Later on, we can save it into a txt file and use it as a message transfer loop, or we can translate between friends. 

import random

class TaskError(Exception):
    pass

# alphabets = "abcdefghijklmnopqrstuvwxyz"

# def randomAssign(assigningList):
#     for i in range(6):
#         if i<3:
#             assigningList.insert(0,random.choice(alphabets))
#         else:
#             assigningList.insert(len(assigningList),random.choice(alphabets))
#     return assigningList

# def coding(message):
#     messageLength = len(message)
#     if messageLength<3:
#         tempList = list(message)
#         tempList.reverse()
#         codedMessage = "".join(tempList)
#         print(f"Your Message In The Secret Language is Given Below:\n{codedMessage}")
#     else:
#         tempList = list(message)
#         firstLetter = tempList[0]
#         tempList.pop(0)
#         tempList.append(firstLetter)
#         codedMessage = "".join(randomAssign(tempList))
#         print(f"Your Message Coded In The Secret Language is Given Below:\n{codedMessage}")


# def decoding(message):
#     messageLength = len(message)
#     if messageLength<3:
#         tempList = list(message)
#         tempList.reverse()
#         decodedMessage = "".join(tempList)
#         print(f"Your Message Decoded From The Secret Language is Given Below:\n{decodedMessage}")
#     else: 
#         tempList = list(message)
#         for i in range(6):
#             if i<3:
#                 tempList.pop(0)
#             else:
#                 tempList.pop(len(tempList)-1)
#         originalFirstLetter = tempList[len(tempList)-1]
#         tempList.pop()
#         tempList.insert(0,originalFirstLetter)
#         decodedMessage = "".join(tempList)
#         print(f"Your Message Decoded From The Secret Language is Given Below:\n{decodedMessage}")

# task = input("Do You Want To Code or Decode?: ")
# # if not task.title() == "Code" or not task.title() == "Decode":
# #     raise TaskError("Invalid Task Was Assigned!\nAllowed Tasks: 'Code' or 'Decode'")
# # elif task.title() == "Code":
# #     coding_message = input("What do you want to code in the secret language?: ")
# #     coding(coding_message)
# # elif task.title() == "Decode":
# #     decoding_message = input("What do you want to decode from the secret language?: ")
# #     decoding(decoding_message)
# # else:
# #     raise UnknownError("An Unknown Error Occured While Executing")
     

# if task.title() == "Code":
#     coding_message = input("What do you want to code in the secret language?: ").lower().strip()
#     coding(coding_message)
# elif task.title() == "Decode":
#     decoding_message = input("What do you want to decode from the secret language?: ").lower().strip()
#     decoding(decoding_message)
# else:
#     raise TaskError("Invalid Task Was Assigned!\nAllowed Tasks: 'Code' or 'Decode'")



#! But it was working fine. The main issue was that when I watched the solution video, there was a pretty short and fascinating solution, but it depends on what clicked in my mind at that point. One thing is for sure: I'll try to replicate in that way too using my own mind and see how things work. 


#* tryin with course's approach
import string
lowercase_alphabets = string.ascii_lowercase

def random_assigner(message):
    random_start = ""
    random_end = ""
    for i in range(3):
        random_start = random_start + random.choice(lowercase_alphabets)
        random_end = random_end + random.choice(lowercase_alphabets)
    message = random_start + message + random_end
    return message

task = input("Do You Want To Code or Decode?: ")
coding = True

if task.title() == "Code":
    given_string = input("What do you want to code in the secret language?: ").strip()
    coding = True
elif task.title() == "Decode":
    given_string = input("What do you want to decode from the secret language?: ").strip()
    coding = False
else:
    raise TaskError("Invalid Task Was Assigned!\nAllowed Tasks: 'Code' or 'Decode'")

# given_string = input("Enter your input: ").strip()
words = given_string.split(" ")

if(coding):
    new_words = []
    for word in words:
        if(len(word)>=3):
            word = word[1:] + word[0]
            new_word = random_assigner(word)
            new_words.append(new_word)
        else:
            new_words.append(word[::-1])    #* reverses a string
    final_string = " ".join(new_words) 
else:
    new_words = []
    for word in words:
        if(len(word)>=3):
            word = word[3:-3]
            new_word = word[-1]+word[:-1]
            new_words.append(new_word)
        else:
            new_word = word[::-1]
            new_words.append(new_word)
    final_string = " ".join(new_words) 

print(final_string)