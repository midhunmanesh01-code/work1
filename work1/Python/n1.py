while True:
    n=int(input("Enter the Height: "))
    if n>0 and n<9:
        break
for i in range(n):
    for j in range(n):
        if (i+j<n-1):
            print(" ",end=" ")
        else:
            print("#",end=" ")
    print()