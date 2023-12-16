# sum of 1st n odd numbers
n = 1
s = 0
i = 1
N = int(input("Number of odd numbers: "))
while i <= N:
    s = s + n
    n = n + 2
    i = i + 1
print("Sum of odd numbers: ", s)