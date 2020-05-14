s=input("Enter a string:")
ds=""
for x in s:
    if s.count(x)>1:
        ds=ds+x
if ds=="":
    print("DUPLICATE elements are:")
    print("None")
else:
    print("DUPLICATE elements are:")
    print(ds)