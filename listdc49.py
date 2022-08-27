a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
count=0
while i<len(a):
    if a[i]=='f':
        count=count+1
    i=i+1
print(count)