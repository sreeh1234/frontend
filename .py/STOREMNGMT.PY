 # STORE MANAGEMENT SYSTEM
client=[{'id':100, 'name':'raju', 'email':'raju@gmail.com', 'phno':7582356798,'password':2468},{'id':101, 'name':'ramu', 'email':'ramu@gmail.com', 'phno':9047546700,'password':1234}]
product=[{'id': 100, 'name': 'football', 'quantity': 20, 'price': 500},{'id': 101, 'name': 'bat', 'quantity': 30, 'price': 1000}]
while True:
    print('''
    1.Register
    2.login
    3.exit
''')
    ch=int(input('enter choice'))
    if ch==1:
        if len(client)==0:
            id=100
        else:
            id=client[-1]['id']+1    
            print(id)
        name=input('enter name')
        email=input('enter email')
        phno=int(input('enter phno'))
        password=int(input('enter password'))
        client.append({'id':id, 'name':'name', 'email':'email', 'phno':phno, 'password':'password'})
    elif ch==2:
        name=input('enter name')
        password=int(input('enter password'))
        if name=='admin' and password==12345:
                print('ADMIN LOGIN SUCCESSFUL')
                while True:
                    print(''' 
                    1.add stock
                    2.update stock
                    3.view stock
                    4.exit
        ''')       
                    ch=int(input('enter choice'))
                    if ch==1:
                        if len(product)==0:
                            id=100
                        else:
                            id=product[-1]['id']+1    
                            # print(id)
                        name=input('enter name of the product')
                        quantity=int(input('enter quantity'))
                        price=int(input('enter price'))
                        product.append({'id':id, 'name':'name','quantity':quantity,'price':price,}) 
                        print(product)
                    elif ch==2:
                            id=int(input('enter id'))        
                            f1=0
                            for i in product:
                                if i['id']==id:
                                    f1=1
                                    i['name']=input('enter new name')
                                    i['quantity']=int(input('enter quantity'))
                                    i['price']=int(input('enter price'))
                                    print(product)
                                    print('UPDATE SUCCESSFULL')
                    elif ch==3:
                            print('{:<10}{:<15}{:<20}{:<15}'.format('id','Name','stock','price'))
                            print('-'*50)  
                            for i in product:
                                print('{:<10}{:<15}{:<20}{:<15}'.format(i['id'],i['name'],i['quantity'],i['price']))   
                                break
                    elif ch==4:
                        break  

                    else:
                        print('invalid choice')
                    if name.isdigit():
                        name=int(name)
                    for i in user:
                        if i['id']==100 and i['password']==password:
                            print('user login')
                    f=2
                    while True:
                        print('''
                1.view product
                2.add to cart
                3.view cart
                4.logout
    ''')      
                        sub_ch= int(input('enter choice'))
                        if sub_ch==1:
                                print(book)          
    elif ch==3:
        break    
        