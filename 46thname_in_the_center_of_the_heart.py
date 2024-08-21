num = int(input("Enter the number of rows: "))
msg = input("Enter any message: ")
n = num // 2

# Upper part of the heart
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1), end="")
    if num % 2 == 0:
        print(" " * (2 * (n - i - 1)), end="")
    else:
        print(" " * (2 * (n - i - 1) + 1), end="")
    print("* " * (i + 1))

# Middle row with the message
print("* " * ((num - 1) // 2) + " ".join(msg) + " * " * ((num - 1) // 2))

# Lower part of the heart (inverted pyramid)
for i in range(num, 0, -1):
    print(" " * (num - i) + "* " * i)
