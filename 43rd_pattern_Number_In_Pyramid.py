num = int(input("Enter The Number Of Rows: "))

# Outer loop for rows
for i in range(1, num + 1):
    # Inner loop for leading spaces
    for j in range(1, num - i + 1):
        print(" ", end="")
    
    # Inner loop for descending numbers
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Inner loop for ascending numbers
    for j in range(2, i + 1):
        print(j, end="")
    
    # Move to the next line after each row
    print()
