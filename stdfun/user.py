from data import product

def viwpro():
    print('{:<9}{:<20}{:<10}{:<10}'.format('id','Name','quantity','price'))
    print('-'*50)  
    for j in product:
        print('{:<9}{:<20}{:<10}{:<10}'.format(j['id'],j['name'],j['quantity'],j['price']))   
        
def atc(users):
    id=int(input('enter id'))
    f1=0   
    for j in product:
        if j['id']==id:
            f1=1
            if j['quantity']>0:
                users['products'].append(id)
                j['quantity']-=1
            else:
                print(' Product Out Of Stock')
    if f1==0:
        print('Product Not Available')
        
def viwcrt(users):
    if len(users['products'])==0:
        print('No Products')
    else:
        a=1
        for pro in product:
            if pro['id'] in i['products']:
                print(a,'.',pro['name'])
                a+=1
             
             