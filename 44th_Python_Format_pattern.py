# num = int(input("Enter The Number Of Rows:"))
# n = 1
# for i in range(num):
#     for j in range(i+1):
#         print(format(n,"<4"),end="")
#         n=n+1
#     print()


num = int(input("Enter The Number Of Rows: "))

for i in range(1, num + 1):
    for j in range(1, num - i + 1):
        print(format(" ","<3"),end="")
    for j in range(i, 0, -1):
        print(format(j,"<3"), end="")
    for j in range(2, i + 1):
        print(format(j,"<3"), end="")

    print()
