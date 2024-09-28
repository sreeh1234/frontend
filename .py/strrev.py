# a=input('enter a str')
# print(a)
# rev=''
# for i in a:
#         rev=i+rev
# print(rev)        


a=input('enter a str')
rev=''
l=len(a)
i=0
while i<l:
#  print(a[i])
    rev=a[i]+rev
    i+=1
print(rev)