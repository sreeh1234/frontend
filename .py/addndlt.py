# APPEND METHOD

# l=[1,2,3]
# l.append(100)
# l.append([10,11])
# print(l)

# EXTEND METHOD

# l=[1,2,3,11,22,33]
# print(l)
# l.extend([10,11])
# print(l)

# INSERT METHOD

# l=[1,2,11,22]
# print(l)
# l.insert(2,100)
# print(l)

# DELETE METHOD:clear

# l=[1,1,1,1,1]
# print(l)
# l.clear()
# print(l)

# pop

# l=[1,2,3,3,2,1]
# l.pop()
# print(l)

# l=[1,2,3,3,2,1]
# l.pop()
# print(l)

# remove      

# l=[11,222,3333]
# l.remove(11)
# print(l)

# del        keytype in python to dlt element

# l=[11,222,3333]
# del l[2]
# print(l)

# copy method

# l=[1,2,3]
# l1=l
# print(id(l1))
# print(id(l))
# l1.pop()

# copy method 2

# l=[1,2,3]
# l1=l.copy()
# print(id(l))
# print(id(l1))
# l.pop()

# l=[10,11,8,5,2,12]
# l.append(10)
# l.sort()
# print(l)
# print(l.index(10))
# print(l.count(10))


# l=[10,11,8,5,2,12,10]
# print (l)
# for i in l:
#  if i%2==0:
#     print(i)

# l=[10,11,8,5,2,12,10]
# print (l)
# for i in l:
#  if i%2!=0:
#     print(i)

# adding of str n int

# l=[10,11,8,5,2,12,10,'abc','ab']

# print (l)
# a=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         a=a+i
# print(a,"is the total sum")

# remove duplicate

# li=[1,2,3,4,5,2,4,6]
# print(li)
# l=[]
# for i in li:
#     if i not in l:
#         l.append(i)

# reverse of str elements
        
l=['apple','orange','kiwi']
print(l)
for i in l:
        print(i[::-1])






