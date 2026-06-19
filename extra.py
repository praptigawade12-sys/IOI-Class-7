n1 = int(input("Enter the start of the list:"))
n2 = int(input("Enter the end of list: "))
l1 = []

for i in range(n1,n2+1):
    l1.append(i**2)

print(l1)

l2 = []
l3 = []

for i in range(len(l1)):
    if l1[i] %2 == 0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])

print(l2)
print(l3)