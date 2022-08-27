a=[1, 2, 3, 4, 5, 6]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i],a[i+1]
#     b.append(c)
#     i=i+1
# print(b)




# a=["meghana","megha","meg"]
# i=0
# max=0
# while i<len(a):
#     b=len(a[i])
#     if max<b:
#        max=b
#        c=a[i]
#     i=i+1
# print(c,max)
    
a=[5,2,0,1,10,9,7,3]
i=0
c=[]
d=[]
while i<len(a):
    if a[i]%2==0:
        c.append(a[i])
    else:
        d.append(a[i])
    i=i+1
print(d+c)
