# def add():
#     a=int(input('enter first number'))
#     b=int(input('enter second number'))
#     print(a+b)
# def sub():
#     a=int(input('enter first number'))
#     b=int(input('enter second number'))
#     print(a-b)
    
# while True:
#     print('''
#     1.add
#     2.sub
#     3.mul
#  ''')
#     ch=int(input('enter choice'))
#     if ch==1:
#         add()  
#     elif ch==2:
#         sub()        


# b=25
# def sample():
#     global a
#     a=20
#     # b=25
#     c=10
#     print('inside fun',b)
#     return c
# c=sample()
# print(c)


# def add(a,b):
#     print(a+b)
# add(10,5)    
# add(20,14)


# def dtls(name='anu',age=23):
#     print('name',name)
#     print('age',age)
def dtls(*a):
    print(a)    
    
dtls()
dtls(1,2)
dtls(1,2,3,4,5)

def dtls(**a):
    print (a)

dtls(name='anu',age=20,place='ekm')    
