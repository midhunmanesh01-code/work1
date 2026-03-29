def add(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return add(a,b-1)+1

a=int(input("enter: "))
b=int(input("enter:"))
s=add(a,b)
print(s)