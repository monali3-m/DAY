a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
print("Values before swapping are :")
print(a,b)
a=a-b
b=a+b
a=b-a
print("The values after swaping are :")
print(a,b)