num = int(input("Enter The Number Of Rows: "))
n = num//2

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('* ', end='')
    for j in range (2*(n-i-1)):
        print(' ', end='')
    for j in range(i+1):
        print('* ', end='')

    print()

for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print("* ",end="")
    print()