# num = int(input("Enter The Number Of Rows: "))
# for i in range(num, 0, -1):
#     for j in range(num - i):
#         print(" ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()


num = int(input("Enter The Number Of Rows: "))
for i in range(num, 0, -1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()