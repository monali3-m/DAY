element={}
z={}
n=int(input("Enter the number of key value pairs you want to enter :"))
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value :")
    element[key]=value
    print("The dictionary is :")
print(element)
for key,value in element.items():
    if value not in z.values():
        z[key]=value
print("the dictionary after removal of duplicate values is :",z)
    