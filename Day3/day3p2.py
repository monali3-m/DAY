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
List=p(list(string))
print("all permutations :"+", ".join(List))
    