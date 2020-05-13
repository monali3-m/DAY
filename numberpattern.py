for i in range(0,2):
    n=3-i
    for j in range(0,n-1):
        print(n,"*",end=" ")
    print(n)
print("1\n1")
for i in range(0,2):
    for j in range(0,i+1):
        print(i+2,"*",end=" ")
    print(i+2)   
