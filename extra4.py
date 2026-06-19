n = int(input("Enter the length:"))
l = []
for i in range(n):
    a = int(input("Enter the element:"))
    l.append(a)

print(l)
print(min(l))
print(max(l))
print(sum(l))
print(sum(l)/len(l))
print(len(l))