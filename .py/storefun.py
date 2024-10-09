client=[{'id':100, 'name':'raju', 'email':'raju@gmail.com', 'phno':7582356798,'password':2468, 'products':[]},{'id':101, 'name':'ramu', 'email':'ramu@gmail.com', 'phno':9047546700,'password':1234,'products':[]}]
product=[{'id': 100, 'name': 'football', 'quantity': 20, 'price': 500},{'id': 101, 'name': 'bat', 'quantity': 30, 'price': 1000}]

def register():
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
def login():
        name=input('enter name')
        password=int(input('enter password'))
        f=0
        if name=='admin' and password==12345:
                f=1
        if name.isdigit():
            name=int (name)  
            for i in client:
                if i['id']==name and i['password']==password:
                    f=2 
                    client=i 
        if f==0:
            print('invalid name or password')
        return f   
def proadd():
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

def proup():
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
            
def viewpro():
    print('{:<10}{:<15}{:<20}{:<15}'.format('id','Name','stock','price'))
    print('-'*50)  
    for i in product:
        print('{:<10}{:<15}{:<20}{:<15}'.format(i['id'],i['name'],i['quantity'],i['price']))   
        break     
    
def viewprou():
    print('{:<9}{:<20}{:<10}{:<10}'.format('id','Name','quantity','price'))
    print('-'*50)  
    for j in product:
        print('{:<9}{:<20}{:<10}{:<10}'.format(j['id'],j['name'],j['quantity'],j['price']))      

def adc():
    id=int(input('enter id'))
    f1=0   
    for j in product:
        if j['id']==id:
            f1=1
            if j['quantity']>0:
                i['products'].append(id)
                j['quantity']-=1
            else:
                print(' Product Out Of Stock')
    if f1==0:
        print('Product Not Available')              
         

while True:
    print('''
    1.Register
    2.login
    3.exit
''')
    ch=int(input('enter choice'))
    if ch==1:
        register()
    
    elif ch==2:
        f=login() 
        if f==1:
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
                    proadd()
                elif ch==2:
                    proup() 
                elif ch==3:
                    viewpro()   
                elif ch==4:
                    break       
                else:
                    print('invalid choice') 
        elif f==2:
            print('USER LOGIN SUCCESSFUL')   
            while True:
                        print('''
                1.view product
                2.add to cart
                3.view cart
                4.logout
    ''')      
            
                 
                    
                     
        