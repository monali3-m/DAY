s1=int(input("Enter size of list 1:"))
l1=[]
for i in range(s1):
    n1=int(input("Enter the element :"))
    l1.append(n1)
s2=int(input("Enter size of list 2:"))
l2=[]
for i in range(s2):
    n2=int(input("Enter the element :"))
    l2.append(n2)
intersectionList=list(set(l1).intersection(set(l2)))
print("The intersection of List1 and List2 is:",intersectionList)
