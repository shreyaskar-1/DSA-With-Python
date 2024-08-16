num = int(input("Enter the number of rows: "))

# Create a 2D list initialized with zeros
n_list = [[0 for x in range(num)] for y in range(num)]

n = 1
low = 0
high = num - 1
count = int((num + 1) / 2)

for i in range(count):
    # Fill top row from left to right
    for j in range(low, high + 1):
        n_list[low][j] = n
        n += 1

    # Fill right column from top to bottom
    for j in range(low + 1, high + 1):
        n_list[j][high] = n
        n += 1

    # Fill bottom row from right to left
    for j in range(high - 1, low - 1, -1):
        n_list[high][j] = n
        n += 1

    # Fill left column from bottom to top
    for j in range(high - 1, low, -1):
        n_list[j][low] = n
        n += 1

    low += 1
    high -= 1

# Print the 2D list in a square shape
for i in range(num):
    for j in range(num):
        print(n_list[i][j], end="\t")
    print()
