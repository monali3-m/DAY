def arrange(list):
    le=[]
    lo=[]
    for e in list:
        if e%2==0:
            le.append(e)
        else:
            lo.append(e)
    le.sort()
    lo.sort(reverse=True)
    print(le)
    print(lo)
    
    
ll=[]
n=int(input("Enter the size of list :"))
for i in range(n):
    lm=int(input("Enter the list member :"))
    ll.append(lm)
print(ll)
arrange(ll)