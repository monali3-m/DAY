def sum(n):
    i=0
    s=0
    while n!=0:
        l=n%10
        if l==0:
            l=5
            s=s+l*10**i
        else:
            s=s+l*10**i
        n=n//10
        i+=1
    print("sum is:",s)

num =int(input("Enter an integer :"))
sum(num)