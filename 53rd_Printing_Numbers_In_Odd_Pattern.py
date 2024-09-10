num = input("Enter The Odd Length Number : ")
length = len(num)
for i in range (length):
    for j in range (length):
        if i==j or i+ j == length-1:
            print(num [i] , end=" ")
        else:
            print(" ",end =" ")
    print()
