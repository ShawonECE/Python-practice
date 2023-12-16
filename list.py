import random

thislist = ['a', 'ap', 'app', 'appl', 'apple', 'p', 'pp', 'ppl', 'pple', 'p', 'pl', 'ple', 'l', 'le', 'e']
thislist_1 = []
ch = ''
#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist_1 = [20, 13, 40, 50, 23]
#tropical = ["guava", "pineapple", "papaya"]

#if "apple" in thislist:
#    print("Yes, apple is in the list")
#else:
#    print("No, apple is not in the list")
#thislist[1] = "blackcurrant"
#thislist[1:1] = ["blackcurrant", "Watermelon"]  
#thislist.insert(2, "watermelon")
#thislist.append("oreo")
#thislist.extend(tropical)
#thislist.pop(1)
#del thislist[2]
#thislist.clear()
#print(thislist)  
#for i in range(len(thislist)):
#  print(thislist[i])

#newlist = []
#newlist_1 = []
#newlist_2 = []


#for x in thislist:
#  if "a" in x:
#    newlist.append(x)
#newlist = [x for x in thislist if "a" in x]
#newlist_1 = [x for x in thislist if "a" not in x]
#newlist_2 = [x for x in thislist if x != "apple"]

#print(newlist)
#print(newlist_1)
#print(newlist_2)
#thislist.sort()
#thislist_1.sort()
#thislist.sort(reverse = True)
#thislist_1.sort(reverse = True)
#thislist.reverse()
#thislist.pop(0)
#thislist.insert(0, "Jack")
#print(thislist)
#print(str(thislist_1))
#print(thislist_1)
#length = len(thislist)
#for k in range(length):
#    min_str = thislist[k]
#    print(min_str)
#k = int(input("Item no. to remove: "))
#thislist.pop(k)
#print(thislist)

#for i in thislist:
#    for j in i:
#        k = True
#        if i.count(j) == 1:
#            pass
#        elif i.count(j) > 1:
#            k = False
#            break
#    if k == True:
#        thislist_1.append(i)
#    else:
#        continue
#print(thislist_1)

#print(thislist.index('ap'))
#x = []
thislist_3 = [1, 2, 3]
x = random.sample(thislist_3, k = 2)
print(x)