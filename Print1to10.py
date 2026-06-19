edef print1to10(n):
    if (n>10):
        return
    
    print(n)
    print1to10(n+1)

n = int(input("Enter you number: "))
print1to10(n)