# set is repreesnted in curly brackets {}
#  in set we can't include another set or lists


# s={1,2,5,3,2,1}
# print(s)
# s.add(10)    
# print(s)
# s.update({6,7,8,9})
# print(s)
# s.pop()
# print(s)
# s.remove(3)
# print(s)
# s.discard(5)
# print(s)
# s.remove(6)
# print(s)
# s.discard(6)
# print(s )
# s.difference({1,2,3,4,5,6,7})
# print(s)
# s.difference_update({1,2,3,4,4,8,6,7})
# # print(s)
# s.intersection({6,7,1,2,3})
# print(s)
# s.intersection_update({6,7,2,3,12})
# print(s)
# s={1,2,3,4,5,6,7,8}
# print(s)
# s.isdisjoint({2,3,4,5,10})
# print(s)
# s.issubset({1,2,3,5})
# s.union({11,22,33,44})
# # print(s)
# s.symmetric_difference({1,3,10,11,22})
# print(s)




# l=[1,2,3,4,5,6,6,6,7,8,7,8]
# print(l)
# s=set(l)
# print(s)
# l=list(s)
# print(l)




# l=[]
# t=()
# s=set()


# l=[1,2,3,{10,11}]
# print(l[3])
# l[3].add(12)
# print(l)


l=[1,2,[10,{5,6}],4]
print(l[2][1])
l[2][1].add(12)
print(l)
