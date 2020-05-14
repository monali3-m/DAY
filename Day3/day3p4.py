list=[]
c=0
n=int(input("Enter the size of the list :"))
for i in range(n):
    le=int(input("Enter the element:"))
    list.append(le)
print("Duplicate elements is:")    
for i in range(n):
    for j in range(i+1,n):
        if list[i]==list[j]:
            c=c+1
            print(list[i])
           
if c==0:
    print("None")