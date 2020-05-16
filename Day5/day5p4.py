def knapsack(W,wt,val,n):
    if n==0 or W==0:
        return 0
    for i in range(n):
        for j in range(i+1,n):
            if wt[i]+wt[j]==W:
                return val[i]+val[j]
            
    
val=[]
wt=[]
W=int(input("enter the value of maximum weight :"))
n=int(input("enter the number of items:"))
for i in range(n):
    vm=int(input("enter the value:"))
    wm=int(input("enter the weight :"))
    val.append(vm)
    wt.append(wm)
print(val)
print(wt)
print("The value for maximum weight is :")
print(knapsack(W,wt,val,n))