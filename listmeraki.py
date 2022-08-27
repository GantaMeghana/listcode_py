numbers=[50,40,23,70,56,12,5,10,71]
# count=0
# i=0
# while i<len(numbers):
#     if 20<numbers[i]<=40:
#        count=count+1
#     i=i+1
# print("the numbers between the 20 and 40 is",count)

# numbers=[50,40,23,70,56,12,5,10,8]
# i=0
# max=0
# while i<len(numbers):
#     if max<numbers[i]:
#        max=numbers[i]
#     i=i+1
# print("maxium of number",max)

# a=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# b=len(a)
# index=0
# while index<b:
#     print(a[index])
#     index=index+1

# num=[50,40,23,70,56,12,5,10,7]
# i=0
# c=0
# while i<len(num):
#     if 20<num[i]<=40:
#         c=c+1
#     i=i+1
# print("print the numbers between 20 and 40:",c )

# num=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# while i<len(num):
#     if max<num[i]:
#         max=num[i]
#     i=i+1
#     print(max)

# num=[50,40,23,70,56,12,5,10,7]
# min=num[0]
# for i in num:
#     if min>i:
#         min=i
# print(min)

# p=['delhi','gujarath','rajastan','punjab','kerala']
# p.reverse()
# print(p)


# p=['delhi','gujarath','rajastan','punjab','kerala']
# i=-1
# while i>=-5:
#     print(p[i])
#     i=i-1

# binery_numbers=[1,0,0,1,1,0,1,1]
# l=len(binery_numbers)
# i=l-1
# a=0
# sum=0
# while i>-1:
#     sum=sum+binery_numbers[i]*(2**a)
#     i-=1
#     a=a+1
# print(sum)

# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]

# print (type(magic_square))
# print(type(magic_square[0]))
# print(type(magic_square[1]))

# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2]))

# list1= [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# i=0
# while i<len(list1):
#     if list1[i]  not in list2:
#        list3.append(list1[i])
#     i=i+1
# print(list3)

# list3=[]
# i=0
# while i<len(list1):
#     if list1[i]  not in list2:
#        list3.append(list1[i])
#     i=i+1
# print(list3)

# list2 = [2,3,1,0,6,7]
# list3=[]
# i=0
# while i<len(list1):
#     if list1[i]  not in list2:
#        list3.append(list1[i])
#     i=i+1
# print(list3)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# a=sum(marks[0])
# b=sum(marks[1])
# c=sum(marks[2])
# l1=len(marks[0])
# l2=len(marks[1])
# l3=len(marks[2])
# print("average of 1 year",a//l1)
# print('average of 2 year',b//l2)
# print('average  of 3 year',c//l3)

# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         b=n[i]+n[j]
#         s=[n[i],n[j]]
#         if number==b:
#             a.append(s)
#         j=j+1
#     i=i+1
# print(a)

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# i = 0
# while i < length:
#    print(students[i] + str(marks[i]))
#    i+=1


# e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# count=0
# count1=0
# while i<len(e):
#     if e[i]%2==0:
#        count=count+1
#     else:
#         count1=count1+1
#     i=i+1
# print("even numbers",count)
# print('odd numers',count1)

# e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# while i<len(e):
#     if e[i]%2==0:
#         sum=sum+e[i]
#     else:
#         sum1=sum1+e[i]
#     i=i+1
# print("even",sum)
# print('odd',sum1)

# e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# while i<len(e):
#     if e[i]%2==0:
#         sum=sum+e[i]
#     i=i+1
# print('even',sum//4)
# print("odd",sum//4)


# a = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# count=0
# count1=0
# count2=0
# while i<len(a):
#     if a[i]>10000000:
#         count=count+1
#     elif a[i]>100000:
#         count1=count1+1
#     else:
#         count2=count2+1
#     i=i+1
# print("crorepati",count)
# print("lakhpati",count1)
# print("dilwalw",count2)

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# b=[]
# while i<len(n):
#     if n[i] not in b:
#         b.append(n[i])
#     i=i+1
#     print(b)

# name = ["Savitri", "Phule", "26"]
# # Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print(name[1]+name[2])
# # Code mei dekhiye naam theek se print kyu nahi ho raha


# a= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     n=[]
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     n.append(a[i])
#     n.append(count)  
#     if n not in b:
#      b.append(n[i])
# i=i+1
#print(b)

# n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i=0
# b=[]
# while i<len(n):
#     if n[i]  not in b:
#         b.append(n[i])
#     i=i+1
# print(b)

# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# max=0
# ind=0
# while i<len(a):
#     b=len(a[i])
#     if max<b:
#         max=b
#         ind=a[i]
#     i=i+1
# print(max,ind)


# a=[1,2,3,1,2,2]
# i=0
# count=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         count=count+1
#     i=i+1
# print(b)


# a=[4,6,4,3,3,4,3,4,3,8]
# i=0
# k=3
# count=0
# while i<len(a):
#     if a[i]==k:
#         count=count+1
#     i=i+1
# print(count)


# a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# i=0
# k=int(input("enter the num"))
# b=[]
# while i<len(a):
#     j=i+1
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     if count>=k:
#         b.append(a[i])
#     i=i+1
# print(b)

                                                                    
# a=[4, 5, 5, 5, 3, 8]



# a=[1, 1, 1, 64, 23, 64, 22, 22, 22]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     if c>1:
#         if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b)

# a=[1, 2, 3]
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=j and j!=k and k!=i and j!=i and i!=k and k!=j:
#                 print(i,j,k) 

# a=[0,9,5]
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=j and j!=k and k!=i and i!=k and j!=i and k!=j:
#                 print(i,j,k)

# a=[1, 1, 2, 3, 4, 5, 1, 2]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=1:
#        b.append(a[i])
#     i=i+1
# print(b)


# a=[5, 6, [], 3, [], [], 9]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])!=list:
#         b.append(a[i])
#     i=i+1
# print(b)
  

# a = [2, -7, 5, -64, -14]
# i=0
# count=0
# count1=0
# while i<len(a):
#     if a[i]>0:
#         count=count+1
#     else:
#         count1=count1+1
#     i=i+1
# print("positive no:",count)
# print("negitive:",count1)

# start=-4
# end=3
# i=start
# while i<end:
#     if i<0:
#       print(i,end=" ")
#     i=i+1    


# start=-3
# end=4
# i=start
# while i<end:
#     if i<0:
#       print(i,end=" ")
#     i=i+1

# start=-4
# end=5
# i=start
# while i<end:
#     if i>=0:
#         print(i)
#     i=i+1

# start=-3
# end=4
# i=start
# while i<end:
#     if i>0:
#         print(i)
#     i=i+1

# a=[34.67, 12, -94.89, 'Python', 0, 'C#']
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#         print(b)
#     i=i+1


# a=[1234, 922, 1984, 19372, 100]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             print("false")
#         j=j+1
#     i=i+1  


# a=['aabc', 'abc', 'ab', 'a']
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             print("true")
#         j=j+1
#     i=i+1

# a=['aabc', 'abc', 'ab', 'ha']
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             print("false")
#         j=j+1
#     i=i+1

# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# c=[]
# while i<len(a)-1:
#     b=a[i]+a[i+1]
#     c.append(b)
#     i=i+2
# print(c)

# a=['1', '2', '3']
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i]+a[i+1]
#     b.append(c)
#     i=i+2
# print(b)

# a=[1, 2, 3, 4, 5, 6]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i],a[i+1]
#     b.append(c)
#     i=i+1
# print(b)

# a=[[1, 2, 4], [2, 4, 4]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a):
#         sum=sum+int(a[i][j])
#         j=j+1
#         b.append(sum)
#     i=i+1
# print(b)

# a=[5,2,0,1,10,9,7,3]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]%2==0 :
#     #    print(a[i])
#        b.append(a[i])
#     else:
#         # print(a[i])
#         c.append(a[i])
#     i=i+1
# print(b+c)

# a="https://www.w3resource.com/python-exercises/list/"
# l=['.com', '.edu', '.tv']
# # print(a)
# def my(a,l):
#     for j in range(len(l)):
#         if l[j] in a:
#             return True
#         else:
#             return False
# print(my(a,l))





# a=[1,2,3,[4,5],6,7,[8,9]]
# i=0
# sum=0
# while i<len(a):
#      if type(a[i])==list:
#           j=0
#           while j<len(a[i]):
#                sum+=a[i][j]
#                j=j+1
#      else:
#           sum+=a[i]
#      i=i+1
# print(sum)

# i=0
# sum=0
# while i<len(b):
#      sum=sum+b[i]
#      i=i+1
# print(sum)
# i=0
# c=[]
# d=[]
# while i<len(b):
#      if b[i]%2==0:
#           c.append(b[i])
#      else:
#           d.append(b[i])
#      i=i+1
# print("even no::",c)
# print("odd no:",d)
     
# a=[1,4,4,5,6,1,2,6]
# # i=0
# # b=[]
# # while i<len(a):
# #      if a[i] not in b:
# #         b.append(a[i])
# #      i=i+1
# # print(b)

a=[110,100,1010,1110]
l=[]
for i in range(len(a)) :
     a[i]=str(a[i])
     s=""
     for j in range(len(a[i])):
          if a[i][j]!="0":
               s+=a[i][j]
     l.append(int(s))
print(l)


# a=[110,100,1010,1110]
# l=[]
# for i in range(len(a)):
#     a[i]=str(a[i])
#     s=""
#     for j in range (len(a[i])):
#         if a[i][j]!="0":
#             s=s+a[i][j]
#         l.append(s)
# print(l)


# a=[1,2,0,3,4,0,5,6,7,0,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(1)
#     else:
#         b.append(0)
#     i=i+1
# print(b)


# a=[0,1,1,0,1,0]
# i=0
# b=[]
# while i<len(a):
#     k=a[:i]
#     j=0
#     c=0
#     while j<len(k):
#         if k[j]==0:
#             c=c+1
#         j=j+1
#     b.append(c)
#     i=i+1
# print(b)

# a=["pf23","98yt","76we"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=""
#     while j<len(a[i]):
#         if a[i][j]>"a" and a[i][j]<="z":
#             sum=sum+a[i][j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)
            

# a=["aa20","bb30","cc40"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=" "
#     while j<len(a[i]):
#         if a[i][j]>="a" and a[i][j]<="z":
#             sum=sum+a[i][j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)


# a=["a3b4c5"]
# c=ascii_lowercase
# i=0
# b=[]
# sum=""
# while i<len(a):
#     c=ascii_lowercase
#     sum=sum+c[3::]
#     i=i+3
#     b.append(sum)
# print(b)

# a=["a3b4c5"]
# c=ascii_lowercase
# i=0
# b=[]
# while i<len(a):
#     if c[i]>="a" and c[i]<="d":
#         b.append(a)
#     elif c[i]>="b"  and c[i]<=
# print(b)    
        
# a=["salony","meghana","shasirekha"]
# i=0
# max=0
# c=0
# while i<len(a):
#     b=len(a[i])
#     if max<b:
#         max=b 
#         c=a[i]
#     i=i+1
# print(max,c)       

# import random
# a=["priti","kale","python"]
# i=0
# b=[]
# while i<len(a):
#     k=random.shuffle(a[i])
#     print(k)
#     b.append(k)
#     i=i+1
# print(b)

# print(random.shuffle(a))
# print(k)


# a=([1,1,1,1],2)
# i=0
# b=[]
# while i<len(a):
#     if 

# a=[[1,2,3],[1,2,3,],[1,2,3,4,]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
#     print(sum)
      

# a=[1,2,3,4,5,6,7]
# i=0
# b=[]
# s=0
# while i<len(a):
#     s=a[i]**2+1
#     b.append(s)
#     i=i+1
# print(b)

# day = int(input("Input birthday: "))
# month = input("Input month of birth (e.g. march, july etc): ")
# if month == 'december':
# 	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# elif month == 'january':
# 	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# elif month == 'february':
# 	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# elif month == 'march':
# 	astro_sign = 'Pisces' if (day < 21) else 'aries'
# elif month == 'april':
# 	astro_sign = 'Aries' if (day < 20) else 'taurus'
# elif month == 'may':
# 	astro_sign = 'Taurus' if (day < 21) else 'gemini'
# elif month == 'june':
# 	astro_sign = 'Gemini' if (day < 21) else 'cancer'
# elif month == 'july':
# 	astro_sign = 'Cancer' if (day < 23) else 'leo'
# elif month == 'august':
# 	astro_sign = 'Leo' if (day < 23) else 'virgo'
# elif month == 'september':
# 	astro_sign = 'Virgo' if (day < 23) else 'libra'
# elif month == 'october':
# 	astro_sign = 'Libra' if (day < 23) else 'scorpio'
# elif month == 'november':
# 	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :",astro_sign)


# a=[[1,2,3],[2,3,4]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         # sum=sum+1
#         j=j+1
#     i=i+1
# print(sum)
