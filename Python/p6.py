str=input("E;")
vowels="aeiouAEIOU"
c=0
v=0
d=0
for char in str:
    if char.isdigit():
        d=d+1
    elif char in vowels:
        v=v+1
    else:
        c=c+1
print(c,v,d)