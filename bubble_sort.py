li = [10, 2, 5, 1, 9, 20, 17]
n = len(li)
temp = 0

for i in range(n):
    for j in range(n-i-1):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            
print(li)