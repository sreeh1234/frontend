user=[{'id':100, 'name':'achu', 'email':'achu@gmail', 'phno':123456, 'password':'achu','books':[]}, {'id':101, 'name':'akhil', 'email':'akhil@gmail', 'phno':123435445, 'password':'akhil','books':[]}]
book=[{'id':100,'name':'thenaliraman', 'stock':5, 'price':50}, {'id':101,'name':'gandhi before india', 'stock':10, 'price':100}]
while True:
    print('''
    1.Register
    2.login
    3.exit
''')
    ch=int(input('enter choice'))
    if ch==1:
        if len(user)==0:
            id=100
        else:
            id=user[-1]['id']+1    
            print(id)
            name=input('enter name')
            email=input('enter email')
            phno=int(input('enter phno'))
            password=input('enter password')
            user.append({'id':id, 'name':'name', 'email':'email', 'phno':phno, 'password':'password'})
    elif ch==2:
            uname=input('enter uname')    
            password=input('enter password')   
            f=0
            if uname=='admin' and password=='admin':
                print('admin login')
                f=1
                while True:
                    print(''' 
                    1.add book
                    2.update book
                    3.delete book
                    4.view book
                    5.view user
                    6.logout
    ''')                
                    sub_ch=int(input('enter ur choice'))
                    if sub_ch==1:
                            if len(book)==0:
                              id=100
                            else:
                                id=book[-1]['id']+1    
                                print(id)
                                name=input('enter name')
                                stock=int(input('enter stock'))
                                price=int(input('enter price'))
                                user.append({'id':id, 'name':'name', 'stock':stock, 'price':price})
                    elif sub_ch==2:
                            id=int(input('enter id'))        
                            f1=0
                            for i in book:
                                if i['id']==id:
                                    f1=1
                                    i['name']=input('enter new name')
                            if f1==0:
                                print('book not available')        
                    elif sub_ch==3:
                            id=int(input('enter id'))        
                            f1=0
                            for i in book:
                                if i['id']==id:
                                    f1=1
                                    book.remove(i)
                            if f1==0:
                                print('book not available')  
                    elif sub_ch==4:
                            print('{:<8}{:<12}{:<20}{:<10}'.format('id','Name','stock','price'))
                            print('-'*50)  
                            for i in book:
                                print('{:<8}{:<12}{:<20}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))   
                            break
                    else:
                        print('invalid choice')          
            if uname.isdigit():
                uname=int(uname)
            for i in user:
                if i['id']==uname and i['password']==password:
                    print('user login')
                    f=2
                    while True:
                        print('''
                1.view book
                2.lend book
                3.return book
                4.books in hand 
                5.logout
    ''')                
                        sub_ch= int(input('enter choice'))
                        if sub_ch==1:
                            print(book)
                        elif sub_ch==2:
                            id=int(input('enter id'))
                            f1=0
                            for j in book:
                                if j['id']==id:
                                    f1=1
                                    if j['stock']>0:
                                        i['books'].append(id)
                                        j['stock']-=1
                                    else:
                                        print('out of stock')
                            if f1==0:
                                print('book not available') 
                        elif sub_ch==3:
                            id=int(input('enter id'))
                            f1=0
                            for j in book:
                                if j['id']==id and id in i['books']:
                                    f1=1
                                    j['stock']+=1
                                    i['books'].remove(id)
                            if f1==0:
                                print('book no available')    
                        elif sub_ch==4:
                            if len(i['books'])==0:
                                print('no books')
                            else:
                                print(i['books'])    
                        elif sub_ch==5:
                            break        
                        else:
                            print('invalid choice')                  

            if f==0:
                print('invalid uname or password')  
            elif ch==3:
                break
            else:
                print('invalid choice')                     
    