n = int(input("Enter the number of rows : "))
for row in range (n,0,-1):
    for col in range (row,0,-1):
        print("*",end=" ")
    for col in range (2*(n-row)):
        print(" ",end=" ")
    for col in range(row,0,-1):
        print("*",end=" ")
    print()

for row in range(n):
    for col in range (row+1):
        print("*",end=" ")
    for col in range (2*(n-row-1)):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()