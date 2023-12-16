#file = open("D:\\My Files\\Number\HSC_22 NUM\Txt\Model.txt", "r")
#print(file.read(11))
#print(file.readline())
#print(file.readline())
f = open("file1.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("file1.txt")
print(f.read())