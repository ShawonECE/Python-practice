def ascending_serial():
    m = int(input("Enter the 1st number:" ))
    n = int(input("Enter the 2nd number:" ))
    p = int(input("Enter the 3rd number:" ))


    if m == n and n == p:
        print("The numbers are equal")
    elif m == n and p > n:
        print(m ,"=", n, p,  "is larger")
    elif m == n and p < n:
        print(m,"=", n, p,  "is smaller")
    elif m == p and n > p:
        print(m ,"=", p, n,  "is larger")
    elif m == p and n < p:
        print(m,"=", p, n,  "is smaller")
    elif p == n and m > n:
        print(p ,"=", n, m,  "is larger")
    elif p == n and m < n:
        print(p,"=", n, m,  "is smaller")
    elif m > n and n > p: 
        print ("Largest number:", m)
        print ("2nd Largest number:", n)
        print ("Smallest number:", p)
    elif m > p and p > n:
        print ("Largest number:", m)
        print ("2nd Largest number:", p)
        print ("Smallest number:", n)
    elif n > m and m > p:
        print ("Largest number:", n)
        print ("2nd Largest number:", m)
        print ("Smallest number:", p)
    elif n > p and p > m:
        print ("Largest number:", n)
        print ("2nd Largest number:", p)
        print ("Smallest number:", m)
    elif p > m and m > n:
        print ("Largest number:", p)
        print ("2nd Largest number:", m)
        print ("Smallest number:", n)
    else:
        print ("Largest number:", p)
        print ("2nd Largest number:", n)
        print ("Smallest number:", m)