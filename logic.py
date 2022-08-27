a=int(input("enter a number"))
# i=0
# b=[]
# while i<a:
#     c=int(input("enter a number"))
#     b.append(c)
#     i=i+1
# print(b)

# a=input("enter a charecter")
# i=0
# while i<len(a):
#     if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#         print("vowel",a[i])
#     else:
#         print("cosonent",a[i])
#     i=i+1

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# i=0
# b.reverse()
# while i<len(a):
#     print(a[i],b[i])
#     i=i+1

# a=["1","a","2","b","3","c","4","d"]
# i=0
# b=[]                                                   
# c=[]
# while i<len(a):
#     if type(a[i])!=int:
#       b.append(a[i])
#     else:
#       c.append(a[i])
#     i=i+1
# print(b)


# a=[1,2,2,4,6]
# i=0
# b=[]
# while i<len(a)-1:
#     if a[i]<a[i+1]:
#        b.append(a[i+1])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[0,9,5]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if i!=j and j!=k and k!=i and j!=i and k!=i and i!=j:
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1


# a=[100,200,300,400]
# b=len(a)
# i=b-1
# while i>-1:
#     print((a[i]),end=" ")
#     i=i-1

# a=[1,4,2,3,4,5,7,8,9,6]
# i=0
# k=2
# b=[]
# while i<len(a):
#     if i==k:
#        a.pop(2)
#        b.append(9)
#        k=k+2
#     b.append(a[i])
#     i=i+1
# print(b)

# a=[1,2,3,4,5,6,7,8,9]
# i=0
# sum=0
# product=1
# while i<len(a):
#     if i<5:
#         sum=sum+a[i]
#     else:
#         product=product*a[i]
#     i=i+1
# print("sum",sum)
# print("product",product)



# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# a=[1,2,3,6,8,10]
# i=0
# max=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i=i+1
# print(max)
        
# a=[6,3,6,8,10]
# i=0
# min=a[i]
# while i<len(a):
#     if min>a[i]:
#         min=a[i]
#     i=i+1
# print(min)

    

# a=[2,3,6,8,10]
# i=0
# b=[]
# c=[]
# d=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b+c)

# a=[2,3,6,8,10]
# i=0
# sum=0
# product1
# while i<len(a):
#     sum=sum+a[i]
#     product=product*a[i]
#     i=i+1
# print(([sum,product]))


# a=[1,2,3,4,5]
# i=0
# b=[]        *
# while i<len(a):
#     if a[i]==4:
#       b.append(a[i])
#     i=i+1
# print(b)


# a=[2,4,6,8]
# b=[3,5,7,9]
# c=[]
# p=0
# i=0
# while i<len(a):
#     p=a[i]*b[i]
#     c.append(p)
#     i=i+1
# print(c)

# n=[[8,3,4],
#    [1,5,9],
#    [6,7,2]]
# r1=0
# r2=0
# r3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             r1=r1+n[i][j]
#         elif i==1:
#             r2=r2+n[i][j]
#         else:
#             r3=r3+n[i][j]
#         j+=1
#     i+=1
# if r1==r2==r3:
#         print("row1",r1)
#         print("row2",r2)
#         print("row3",r3)
# else:
#     print("not equal",r1,r2,r3)
# c1=0
# c2=0
# c3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             c1=c1+n[i][j]
#         elif i==1:
#             c2=c2+n[i][j]
#         else:
#             c3=c3+n[i][j]
#         j+=1
#     i+=1
# if c1==c2==c3:
#     print("column1",c1)
#     print("column2",c2)
#     print("column3",c3)
# else:
#     ("not equal",c1,c2,c3)
# d1=0
# d2=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             d1=d1+n[i][j]
#         elif i==1:
#             d2=d2+n[i][j]
#         j+=1
#     i+=1
# if d1==d2:
#     print("diagonal1",d1)
#     print("diagonal2",d2)
#     print("yes it's a magic square")
# else:
#     ("not equal",d1,d2)

# a=["apple"]
# i=0
# b=[]
# for i in a:
#     c=list(i)
#     # b.append(c)
# print(c)


# a=["apple"]
# i=0
# for i in a:
#     c=list(i)
#     print(c)

# n=[[8,3,4],
#   [1,5,9],
#   [6,7,2]]
# i=0
# c1=0
# c2=0
# c3=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#            c1=c1+n[i][j]
#         elif i==1:
#             c2=c2+n[i][j]
#         else:
#             c3=c3+n[i][j]
#         j=j+1
#     i=i+1
# if c1==c2==c3:
#    print(c1)
#    print(c2)
#    print(c3)
# else:
#     print("not equel",c1,c2,c3)
# r1=0
# r2=0
# r3=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             r1=r1+n[i][i]
#         elif i==1:
#             r2=r2+n[i][j]
#         else:
#             r3=r3+n[i][j]

# a=['my','name','is','meghana']
# i=0
# b=" "
# while i<len(a):
#     # j=0
#     # while j<len(a[i]):
#     b=b+a[i]
#     i=i+1
# print(b)

# a=[1,2,3,4,5,6]
# b=[2,3,4,0,6,7]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         c.append(a[i])
#     elif b[i] not in a:
#         c.append(b[i])
#     i=i+1
# print(c)

# a=["meghana"]
# b=[]
# for i in a:
#     c=list(i)
#     # b.append(c)
# print(c)
# i=0
# d=""
# while i<len(c):
#     s=0
#     while s<len(c[i]):  
#         s=c[i],5
#     i=i+1
# print(s)



# a= int(input("enter a number"))
# i=0
# b=[]
# while i<a:
#     c=input("enter a name")
#     b.append(c)
#     d=len(c)
#     if d<5:
#        print(c)
#     i=i+1
# print(b)
# # d=len(c)
# # if len(c)<6:
#     print(c)a= int(input("enter a number"))
# i=0
# b=[]
# while i<a:
#     c=input("enter a name")
#     b.append(c)
#     d=len(c)
#     if d<5:
#        print(c)
#     i=i+1
# print(b)
# # d=len(c)
# # if len(c)<6:

# a=[[1,2,3],[4,5,6],[7,8]]
# i=0
# d=0
# while i<len(a):
#     d=d+sum(a[i])
#     i=i+1
# print(d)
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# i=0
# b.reverse()
# while i<len(a):
#     print(a[i],b[i])
#     i=i+1

# a=input("meghna")
# i=0
# while i<len(a):
#     if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#         print(a[i],"vowl")
#     else:
#         print(a[i],"consonent")
#     i=i+1
    

# a=int(input("enter a number"))
# i=a
# b=[]
# while i>0:
#     c=int(input("enter a number"))
#     b.append(c)
#     i=i-1
# print(b)

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

# a=["apple","banana","cherry"]

# print(a)

# quetion
# a=[5,6,7,12,17]
# i=0
# sum=0
# while i<len(a):
#     if a[i]%2!=0 :
#         sum=sum+a[i]
#     i=i+1
# print(sum)



# a=[1,1,3,3,4,5,4]
# i=0
# while i<len(a):
#     j=0

#     if a[i]==a[i]:
#         a.remove(a[i])
#     else:
#         print(a)
#     i=i+1
# print(a)

# a=["meghna","meg","meghana"]
# i=0
# max=0
# while i<len(a):
#     b=len(a[i])
#     if max<b:
#         max=b
#         c=a[i]
#     i=i+1
# print(max,c)

# a=["ab12","cd34","fg56"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=""
#     while j<len(a[i]):
#         if a[i][j]>="a" and a[i][j]<="z":  
#             sum=sum+a[i][j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)


# a=[7,9,2,5,8,4,3,1]
# print(a[2:7:2])

# for i in range(1,10,1):
#     print(i)
# i=1
# while i<=50:
#     if i%2!=0:
#         print(i)
#     i=i+1

# a=["apple","banana","cherry"]
# a.pop()
# print(a)

# a=[1,2,3,1,2,3,4,5,6]
# b=[]
# for i in a:
#     if  i not  in b:
#        b.append(i)
# print(b)

# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# i=0
# d=[]
# while i<len(a):
#     c=[a[i],b[i]]
#     d.append(c)
#     i=i+1
# print(d)
# a.extend(b)
# print(a)

# n=int(input("enter a number"))
# i=0
# while i<=n:
#     a=(n//100%10)**3
#     b=(n//10%10)**3
#     c=(n%10**3)
#     sum=a+b+c
# if sum==n:
    

# a=[110,100,1010,1110]
# b=[]
# for i in range(len(a)):
#     a[i]=str(a[i])
#     d=""
#     for j in range(len(a[i])):
#         if a[i][j]!="0":
#            d=d+a[i][j]
#     b.append(int(d))
# print(b)

# [j]
# #     b.append(int(d))
# [j]
# #     b.append(int(d))
# print(b)

# def sum(a,b):
#     c=a+b
#     return c
# print(sum(5,7))

# a=lambda a,b:a+b
# print(a(3,5))



# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))


# def display(**a):
#     for i in a:
#         print(i)
# display(a="mba",b="mca")


# def arg_printer(a, b, *args, option=True, **kwargs):
#    print(a, b)
#    print(args)
#    print(option)
#    print(kwargs)
# arg_printer(1, 4, 6, 5, param1=5, param2=6)

# def key(**kwards):
#     print(kwards)
# key(s=7,c=9)


# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1
# i=5
# while i>=1:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1


# str="meghana"
# i=0
# while i<6:
#     j=0
#     while j<=i:
#         print(str[i],end="")
#         j=j+1
#     print()
#     i=i+1


# i=1
# a=1
# while i<=5:
#     b=1
#     while b<=5-1:
#         print(" ",end="  ")
#         b=b+1
#     j=1
#     while j<=a:
#         print("*",end="")
#         j=j+1
#     a=a+2
#     i=i+1
#     print()

# def last(a):
#     b=a%10
#     print(b)
# last(int(input("enter a number")))

# str="python"
# i=0
# while i<=7:
#     j=0
#     while j<=i:
#         print(str[i],end="")
#         j=j+1
#     print()
#     i=i+1

# a=[1,2,3,[],8,[]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])!=list:
#        b.append(a[i])
#     i=i+1
# print(b)


# a=[110,100,1010,101]
# b=[]
# for i in range(len(a)):
#     a[i]=str(a[i])
#     c=""
#     for j in range(len(a[i])):
#         if a[i][j]!="0":
#             c=c+a[i][j]
#     b.append(int(c))
# print(b)

# a=int(input("enter a number"))
# i=1
# while i<=a:
#     n=int(input("enter a  number"))
#     if n<0:
#         print("negitive number")
#     else:
#         print("positive")
#     i=i+1

# def fun(*kargs):
# def fun(a):
#     # a=int(input("enter a number"))
#     i=0
#     b=[]
#     sum=0
#     while i<=a:
#       c=int(input("enter a nuber"))
#       b.append(c)
#       sum=sum+c
#     i=i+1
#     print(b)
#     # print(sum)
# fun(int(input("enter num")))

# i=1
# while i<=100:
#     if i%7==0:
#        print(i)
#     i=i+1


# a=[1110,1010,1111]
# l=[]
# for i in range(len(a)):
#     a[i]=str(a[i])
#     s=""
#     j=0
#     for j in range(len(a[i])):
#         if a[i][j]!="0":
#             s=s+a[i][j]
#     l.append(int(s))
# print(l)