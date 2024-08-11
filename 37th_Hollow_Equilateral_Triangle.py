for row in range (1,5):
    for col in range (1,8):
        if (row == 4) or (row + col == 5) or (col-row==3):
            print("*", end = "")
        else:
            print(end=" ")
    print()