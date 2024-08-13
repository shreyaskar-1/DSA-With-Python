for row in range(5):
    for col in range(5):
        if (row + col ==2) or (col - row ==2) or (row-col == 2) or col + row == 6:
            print("*", end="")
        else:
            print(end=" ")
    print()