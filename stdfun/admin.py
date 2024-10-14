def addstock():
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

def upstk():
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


def viwstk():  
    print('{:<10}{:<15}{:<20}{:<15}'.format('id','Name','stock','price'))
    print('-'*50)  
    for i in product:
        print('{:<10}{:<15}{:<20}{:<15}'.format(i['id'],i['name'],i['quantity'],i['price']))   
        break      