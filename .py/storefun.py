client=[{'id':100, 'name':'raju', 'email':'raju@gmail.com', 'phno':7582356798,'password':2468, 'products':[]},{'id':101, 'name':'ramu', 'email':'ramu@gmail.com', 'phno':9047546700,'password':1234,'products':[]}]
product=[{'id': 100, 'name': 'football', 'quantity': 20, 'price': 500},{'id': 101, 'name': 'bat', 'quantity': 30, 'price': 1000}]

def register():
    ch=int(input('enter choice'))
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
        if name=='admin' and password==12345:
                print('ADMIN LOGIN SUCCESSFUL')        


while True:
    print('''
    1.Register
    2.login
    3.exit
''')