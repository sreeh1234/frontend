# print("4 Fuction Calculator")
# while True:
#     print (" 1.Addition\n 2.subtraction\n 3.division\n 4.Multiplication\n 5.exit\n\n")
#     fun=int(input("Choose a Number"))
#     a=int(input("Enter First Number"))
#     b=int(input("Enter Second Number"))
#     if fun==1:
#         rslt=a+b
#         print("result is",rslt)
#     elif fun==2:
#         rslt=a-b
#         print("result is",rslt) 
#     elif fun==3:
#         rslt=a/b
#         print("result is",rslt)
#     elif fun==4:
#         rslt=a*b
#         print("result is",rslt)
#     elif fun==5:
#         break    
#     else:
#         print("invalid choice") 



while True:
    print(''' 
    1.add
    2.sub
    3.mul
    4.div
    5.mod
    6.exit
    ''')
ch=int(input('choice'))
if ch==1:
    a=int(input('no1'))
    a=int(input('no2'))
    print(a+b)
elif ch==1:
    a=int(input('no1'))
    a=int(input('no2'))
    print(a-b)
elif ch==1:
    a=int(input('no1'))
    a=int(input('no2'))
    print(a*b)
elif ch==1:
    a=int(input('no1'))
    a=int(input('no2'))
    print(a/b)
elif ch==1:
    a=int(input('no1'))
    a=int(input('no2'))
    print(a%b)
else:
    print('invalid')