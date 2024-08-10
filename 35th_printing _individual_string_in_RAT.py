str = input("Enter The String : ")
length = len(str)
print("Length of the string is : ", length)
for rows in range (length):
    for col in range(rows+1):
        print(str[col],end="")
    print()