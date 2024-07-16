num = int(input("enter the numbers: "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()