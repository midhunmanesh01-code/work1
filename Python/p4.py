a=eval(input("Enter the list: "))
l=len(a)
a.sort()


if l%2!=0:
    print(a[l//2])
else:
    m=(a[l//2]+a[l//2 -1])/2
    print(m)