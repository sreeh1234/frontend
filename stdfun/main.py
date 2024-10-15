from reg_log import *
from user import *
from admin import *

while True:
    print('''
1.register
2.login
3.exit
''')
    ch=int(input('enter your choice'))
    if ch==1:
        reg()
    elif ch==2:
        f,users=login() 
        if f==1:
            while True:
                print('''
            1.add stock
            2.update stock
            3.view stock
            4.exit
            ''')
                ch=int(input('enter your choice'))
                if ch==1:
                    addstock()
                elif ch==2:
                    upstk()
                elif ch==3:
                    viwstk()
                elif ch==4:
                    break    
        elif f==2:
            while True:
                print('''
            1.view product
            2.add to cart
            3.view cart
            4.logout          
            ''')
                ch=int(input('enter your choice'))
                if ch==1:
                    viwpro()
                elif ch==2:
                    atc(users) 
                elif ch==3:
                    viwcrt(users)       
                elif ch==4:
                    break    
                            
                        
                        
                    
                
    elif ch==3:
        break    
            
        
    