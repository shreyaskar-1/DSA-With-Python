num = (int(input("Enter The Number Of Rows : ")))
for row in range(num):
    n = row+1
    for col in range(num-row-1):
        print(" ",end="  ")
    for col in range(row+1):
        print(n,end=" ")
    n = n-1
    if row > 0:
        for col in range(row-1):
            print(" ",end=" ")
        for col in range(row+1):
            print(n,end=" ")
            n = n + 1
    print()

for row in range(0,num-1):
    n = num-row
    for col in range(row):
        print(" ",end="  ")
    for col in range(num-row):
        print(n,end=" ")
        n = n - 1
    if row < (num-1):
        for col in range(num-row-2):
            print(" ",end=" ")
        for col in range(row+1):
            n = n + 1
            print(n,end=" ")
            
    print()
    
