# i=0
# j=5
# for row in range (6):
#     for col in range(6):
#         if row ==col:
#             print("*",end="")
#         elif (row == i and col == j):
#             print("*",end="")
#             i=i+1
#             j=j-1
#         else:
#             print(end=" ")
#     print()

i=0
j=4
for row in range (5):
    for col in range(5):
        if row == i and col==j:
            print("*",end="")
            i=i+1
            j=j-1
        elif (row == col):
            print("*",end="")
        else:
            print(end=" ")
    print()