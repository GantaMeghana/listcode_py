a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=0
ind=0
while i<len(a):
    b=len(a[i])
    if max<b:
        max=b
        ind=a[i]
    i=i+1
print(max,ind)