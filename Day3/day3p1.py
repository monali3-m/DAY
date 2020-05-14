s=input("Enter a string :")
n=len(s)
rs=''
while n!=0:
    rs=rs+s[n-1]
    n=n-1
print(rs)