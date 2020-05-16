l=[]
n=int(input("Enter the size of tuple:"))
for i in range(n):
    le=input("Enter the element:")
    l.append(le)
l.sort()
t=tuple(l)
print(t)
