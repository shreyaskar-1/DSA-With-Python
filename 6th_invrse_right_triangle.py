num = int(input("Enter the number of rows: "))
number = int(input("Enter the number of columns: "))

for row in range(num):
    for col in range(number):
        # Conditions to print '*'
        if (col == 0 or col == number - 1) and row != 0 or \
           (row == 0 or row == num // 2) or \
           (col > 0 and col < number - 1 and row == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
