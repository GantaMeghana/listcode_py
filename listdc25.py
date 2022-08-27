a=[4,6,4,3,3,4,3,4,3,8]
i=0
k=3
count=0
while i<len(a):
    if a[i]==k:
        count=count+1
    i=i+1
print(count)