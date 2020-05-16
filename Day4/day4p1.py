l=[]
n=int(input("Enter the size :"))
for i in range(n):
    le=input("Enter the element :")
    l.append(le)
t=tuple(l)
print(t)
a=input("Enter the element whose occurence is to be printed :")
print(t.count(a))