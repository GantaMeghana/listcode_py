# a=[1, 1, 2, 3, 4, 4, 5, 1]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     n=[]
#     count=0
#     while j<len(a):
#         if a[i] in a:
#             if a[i]==a[j]:
#                 count=count+1
#             j=j+1
#     n.append(count)
#     n.append(a[i])
#     if n not in b:
#         b.append(n)
#     i=i+1
# print(b)

a=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
b=[]
while i<len(a):
    j=0
    n=[]
    count=0
    while j<len(a):
        if a[i] in a:
            if a[i]==a[j]:
               count=count+1
            j=j+1
    n.append(count)
    n.append(a[i])
    if n not in b:
        b.append(n)
        i=i+1
print(b)