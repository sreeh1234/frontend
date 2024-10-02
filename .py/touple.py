# Tuple is inmutable it cant be changed
# A single touple can be denoted as t=(1,)
# Tuple donot consider brackets
# It can be also written without brackets


# t=(1,[10,11],2)
# print(t[1])
# t[1].append(12)      we can make changes in list if it is also in the tuple 
# print(t)  

# tuple methods
  
#   t.count()
#   t.index()

# t=(1,2,3,4,1)
# print(t.count(1))
# print(t.index(1))
# print(t.index(1,1))

t=(1,2,3,4,5,2,1)
a=1
print(t.count(a))
pos=0
c=t.count(a)
while c>0:
        p=t.index(a,pos)
        print(p)
        pos=p+1
        c-=1
