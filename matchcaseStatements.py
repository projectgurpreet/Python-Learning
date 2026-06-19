string = input("Write Something: ")
pattern1 = string.endswith("!")
pattern2 = string.endswith("@")
pattern3 = string.endswith("#")

match string:
    case _ if  pattern1: 
        print("The given string ends with !")
    case _ if pattern2:
        print("The given string ends with @")
    case _ if  pattern3:
        print("The given string ends with #")
    case _:
        print("The given string doesn't match pre loaded patterns. it instead ends with",string[len(string)-1])