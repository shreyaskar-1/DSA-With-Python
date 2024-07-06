num = int(input("enter the number"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print(j,end=" ")
    k=k+2
    print()