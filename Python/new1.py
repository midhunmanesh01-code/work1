str=input("Enter: ")
words=str.split()
c=0
for i in words:
    c=c+len(i)
if len(words)>0:
    avg=c/len(words)
else:
    avg=0
print(avg)