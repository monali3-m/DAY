a,b,s,i=-1,1,0,1
n=int(input(""))
while i<=n:
    s=a+b
    print(s)
    a=b
    b=s
    i=i+1