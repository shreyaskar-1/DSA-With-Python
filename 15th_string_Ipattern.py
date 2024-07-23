for row in range (7):
    for col in range (5):
        if row == 0 or row ==6 or (col == 2 and col>1 and col<3):
          print("*",end="")
        else:
           print(end=" ")
    print()