def p(List,String=""):
    Set=set(List)
    stringList=[]
    if len(Set)==1:
        String+="".join(List)
        return list([String])
    for x in Set:
        List1=list(List)
        S=String+x
        List1.remove(x)
        stringList.extend(p(List1,S))
    return stringList


string=input("Enter a string :")
n=int(input("Enter the size of list :"))
ll=[]
rw=[]
for i in range(n):
    le=input("enter :")
    ll.append(le)
print(ll)
List=p(list(string))
rw="".join(List).intersection(ll)
print(rw)
