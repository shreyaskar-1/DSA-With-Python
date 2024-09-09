num = int(input("Enter The Number Of Rows : "))
for i in range (num):
    count = 0
    for j in range (num-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("*",end="")
        if count<i :
            print("A",end='')
            count = count +1
    print()
