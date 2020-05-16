def valuestolen(list,n):
    s=0
    if n==0:
        print("value stolen is :",n)
    elif n==1:
        print("Value stolen is :",list[n])
    else:
        for i in range(0,n,2):
            s=s+list[i]
    print("Value stolen is :",s)
    

l=[]
size=int(input("Enter the size of the list :"))
for k in range(size):
    le=int(input("Enter the item:"))
    l.append(le)
valuestolen(l,size)