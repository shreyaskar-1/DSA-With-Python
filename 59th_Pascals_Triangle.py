num = int(input("Enter the number of rows: "))
list1 = []

# Generating Pascal's Triangle
for i in range(num):
    temp_list = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list1.append(temp_list)

# Printing Pascal's Triangle
for i in range(num):
    # Print leading spaces for formatting
    print(" " * (num - i - 1), end=" ")
    
    # Print the values in the current row
    for j in range(i + 1):
        print(list1[i][j], end="   ")
    
    print()  # Move to the next line
