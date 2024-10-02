# for i in range (6):
#     print (i)

# while (i>0):
#     print("*")
#     i=i-0


# for i in range(5):
#     print("*" *i)

# for i in range(5,0,-1):
#     print("*" *i)

c=0
a=int(input("enter a number"))
temp=a
while(a>0):
        b=a%10
        c=c*10+b
        a=a//10
        print(c)
    


