# num = int(input("Enter The Number Of Rows: "))
# for i in range(num):
#     for j in range(num - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print("")


# num = int(input("Enter The Number Of Rows: "))
# for i in range(0,num):
#     for j in range(0,num - i - 1):
#         print(end=" ")
#     for j in range(0,i + 1):
#         print("*", end=" ")
#     print()

def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+"*"*(i+1))