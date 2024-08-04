i = 0
j = 6

for row in range(4):
    for col in range(7):
        if col == row:
            print("*", end="")
        elif row == i and col == j:
            print("*", end="")
            i = i + 1
            j = j - 1 
        else:
            print(" ", end="")
    print()
