str = input("Enter your string: ")
sub_str = ''
li = []
length = len(str)
print(length)

for i in range(length):
    for j in range(i + 1, length):
        sub_str = sub_str + str[i:j]
        li.append(sub_str)
print(li)