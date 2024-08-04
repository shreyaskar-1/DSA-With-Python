i=0
j=3
for row in range (4):
    for col in range(7):
        if col == 0 or col == 6 or (col==5 and row ==2) or (col==4 and row ==1):
            print("*", end="")
        elif row == i and col==j:
            print("*", end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()