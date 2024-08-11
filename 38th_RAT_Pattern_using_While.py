num = int(input("Enter The Numbers :"))
row = 0
while row < num:
    star = row+1
    while star>0:
        print("*" , end = "")
        star = star - 1
    row = row+1
    print()