a=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
b=[]
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    if c>1:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)
