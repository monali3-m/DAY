def funcshift(list,size):
    c=0
    for k in range(size):
        for m in range(k+1,size):
            if list[k]<list[m]:
               c=list[k]
               list[k]=list[m]
    print(list)          
            
n=int(input("Enter the size of the list :"))
l=[]
for i in range(n):
    le=int(input("Enter member %d :"%(i+1)))
    l.append(le)
print(l)
funcshift(l,n)
