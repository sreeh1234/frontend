print("4 Fuction Calculator")
c="y"
while (c=="y"):
print (" 1.Addition\n 2.subtraction\n 3.division\n 4.Multiplication\n\n")
fun=int(input("Choose a Number"))
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
   if fun==1:
      rslt=a+b
      print("result is",rslt)   
   elif fun==2:
      rslt=a-b
      print("result is",rslt) 
   elif fun==3:
      rslt=a/b
      print("result is",rslt)
   elif fun==4:
      rslt=a*b
      print("result is",rslt)
   else:
      print("wrong entry") 
      print("Do you want to continue?")
      c=str(input("yes/no"))
   if c=="n":
       break
   elif c=="y":
        pass