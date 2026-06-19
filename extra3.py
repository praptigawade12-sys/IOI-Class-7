n = int(input("Enter the length:"))
l = []
for i in range(n):
    a = int(input("Enter the element:"))
    l.append(a)

ones = l.count(1)
zeros = l.count(0)

if ones > zeros:
    print("The weather will be sunny")
elif zeros > ones:
    print("The weather will be rainy")
else:
    print("The weather will be moderate")