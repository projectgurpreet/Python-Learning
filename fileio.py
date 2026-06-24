# f_read = open("trial_file.txt","r")
# # print(f)
# text = f_read.read()
# # print(text)
# f_read.close()

# f_append = open("appendingfile.txt","a")

# f_write = open("writingfile.txt","w") #write mode ki vajah se ye file exist nhi krti thi to isne bana di, lekin agar existing file hone pe ye run krdiya to us existing file ka content erase hojayega
# f_write.write("i wrote this using python")
# f_write.close() #yaha ye close krna important hota h but next method se important ni rehta vo, automatic hojata h

# with open("appendingfile.txt","at") as f:
#     f.write("i did with with \"with\" keyword to append text in this file")

#readline method: reads a single line, to read multiple lines you need a loop. 
# f = open("trial_file.txt","r")
# print(f.readline()) #gives line1 \n
# print(f.readline()) #gives line2 \n
# print(f.readline()) #gives line3 \n
# print(f.readline()) #gives line4 \n
# print(f.readline()) #gives line5 \n
#yaha tune ek baar read krli to neeche 6th line se continue hoga because file open hone ke baad 5 lines tu read kr chuka h bina file ko close kre

# while True: #due to the loop lines keep getting generated, basically upar wali cheez ko automate krdiya. also isse ham kahi bhi rok skte h loop ko. agar .readlines() use krta to saara lines as a list of strings aajati
#     line = f.readline()
#     if not line: 
#         print(line,type(line)) 
#         break 
#     print(line)

# f = open("writing_file","w")
# lines = ["ye line ven h","ye line tiyu h","ye line thri h","ye line phor h","ye line fev h"]
# with open("writingfile.txt","w") as f:
#     f.writelines(lines) #sab ek hi line mein likhdega ye

# with open("writingfile.txt","w") as f:
#     for line in lines:
#         f.write(line + "\n")
# for line in lines:
#     f.writelines(line)

# with open("writingfile.txt","r") as f:
#     print(f.read(25))

with open("writingfile.txt","r+") as f:
   f.seek(7) #7th byte pe pohonch gaya ab ye and ab jo actions honge vo is position se honge
   f.truncate(7)
#    print(f.tell())
#    data = f.read(5)
#print(data)
