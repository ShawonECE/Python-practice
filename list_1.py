#str = 'apple'
#for i in str:
#    k = True
#    if str.count(i) == 1:
#        pass
#    else:
#        k = False
#        break
    
#print(k)
max = 0
max_ind = 0
goals =[11, 14, 3, 8, 4, 20, 5]

for i in range(len(goals)):
    if goals[i] > max:
        max = goals[i]
        max_ind = i
print(max_ind, max)
        