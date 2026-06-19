n = int(input("Enter the length:"))
l = []
for i in range(n):
    a = input("Enter the element:")
    l.append(a)

print(l)

for i in l:
    if (len(i) > 2) and (i[0].lower() == i[-1].lower()):
        print(i,"satisfies both conditions")