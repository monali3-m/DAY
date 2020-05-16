a=[]
c=0
k=""
n=int(input("Enter the size:"))
for i in range(n):
    le=input("Enter")
    a.append(le)
print(a)
t=tuple(a)
for z in t:
    if t.count(z)>c:
        c=t.count(z)
for z in t:
    for z1 in t:
        if (t.count(z)==c and t.count(z1)==c and z!=z1):
            if z<z1:
                k=z
            elif z>z1:
                k=z1
print("The winner is:",k)

    
