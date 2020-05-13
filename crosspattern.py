for i in range(0,8):
    for j in range(0,8):
        if (i==j or j==7-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()