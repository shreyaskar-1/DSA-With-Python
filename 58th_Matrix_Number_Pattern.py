N = int(input("Enter N Value : "))
k = (2*N)-1
low = 0
high = k-1
value = N
matrix = [[0 for i in range (k)] for j in range (k)]
for i in range (N):
    for j in range(low,high+1):
        matrix[i][j] = value
    for j in range(low+1 , high+1):
        matrix[i][j] = value
    for j in range(low+1,high+1):
        matrix[i][j] = value
    for j in range(low+1,high):
        matrix[i][j] = value

    low = low + 1
    high = high - 1
    value = value-1
for j in range (k):
    for j in range (k):
        print(matrix[i][j],end=" ")
    print()
