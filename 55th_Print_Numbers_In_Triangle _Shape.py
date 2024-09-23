# num = int(input("Enter The Number : "))
# for i in range (num):
#     k = 11
#     for j in range (i+1):
#         print(k,end=" ")
#         k = k+111
#     print(k)

num = int(input("Enter The Number : "))
for i in range (num):
    k = 111
    for j in range (num-i-1) :
        print(format(" " ,"<5"),end=" ")
    for j in range (i+1) :
        print(format(k,"<5"),end="")
        k = k+111
    print()