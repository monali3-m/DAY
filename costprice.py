cp=float(input("Enter the cost price of the item:"))
sp=float(input("Enter the selling price of the item:"))
p=sp-cp
pp=(sp-cp)/cp*100
print("The profit is =",pp,"%")
print("For profit percent  to increase by 5 selling price should  be ")
spp=((pp+5)*cp/100)+cp
print(spp)