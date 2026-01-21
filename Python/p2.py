v="aeiouAEIOU"
s=input("e:")
r=" "
for char in s:
    if char not in v:
        r=r+char
print(r)