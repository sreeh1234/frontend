from data import client
def reg():
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
    password=input('enter password')
    f=0
    users=''
    if name=='admin' and password=='admin':
        print('admin login successful')
        f=1
    if name.isdigit():
        name=int(name)
        for i in client:
            if i['id']==name and i['password']==password:
                print('user login successful')
                f=2
                users=i
    if f==0:
        print('invalid name or password')        
    return f,users          