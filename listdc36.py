a=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
c=[]
while i<len(a)-1:
    b=a[i]+a[i+1]
    c.append(b)
    i=i+2
print(c)


