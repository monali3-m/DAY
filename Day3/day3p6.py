def sum(List,size,sum):
    sumList=[]
    if size==1:
        for x in List:
            sumList.append(sum+x)
        return sumList
    L2=list(List)
    for x in List:
        L2.remove(x)
        sumList.extend(Sum(L2,size-1,sum+x))
    return sumList

def summation(List,size):
    sumList=list(List)
    for i in range(2,size+1):
        sumList.extend(Sum(List,i,0))
    number=1
while True:
    if number not in sumList:
        print("the required number is 1")
        break
    number+=1
    
size=int(input("Enter the list size; "))
List=[]
print("Enter the elements :")
for i in range(size):
    List.append(int(input()))
summation(List,size)    
    
    
    
    
    
    
    
    
    
    