print("1. Odd-Even checker\n2.Prime checker\n3.Armstrong checker\n4.Palindrome checker :")
n=int(input("Enter ur choice :"))
if n==1:
    num=int(input("Enter the number to be checked :"))
    if num%2==0:
        print("Even")
    else:
        print("Odd")
elif n==2:
    num=int(input("Enter the number to be checked :"))
    for i in range(2,num):
        if num%i==0:
            print("Composite")
            break
        else:
            print("Prime")
            break
elif n==3:
    num=int(input("Enter the number to be checked :"))
    n1=num
    s=0
    while n1!=0:
        l=n1%10
        s=s+l*l*l
        n1=n1//10
    if (num==s):
        print("Armstrong")
    else:
        print("Not Armstrong")
elif n==4:
    num=int(input("Enter the number to be checked :"))
    n2=num
    z=0
    while n2!=0:
        r=n2%10
        z=(z*10)+r
        n2=n2//10
    if z==num:
        print("Pallindrome")
    else:
        print("Not Pallindrome")
        
        
        
        
        
        
        

    
          
          
          
          
          
          
          
          
          
          
          
          
          
 