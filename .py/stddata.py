l=[{'roll_no':2, 'name':'b','email':'b','cur':'b'},{'roll_no':1, 'name':'a','email':'a','cur':'a'}]
while True:
    print(''' 
    1.add std
    2.view std
    3.update std
    4.delete std
    5.exit
    ''')
    ch=int(input('choice'))
    if ch==1:
        roll_no=int(input('roll_no'))
        name=str(input('name'))
        email=str(input('email'))
        cur=str(input('cur'))
        l.append({'roll_no':roll_no,'name':name,'email':email,'cur':cur})
    elif ch==2:
        print('{:<8}{:<12}{:<20}{:<10}'.format('Roll_no','Name','Email','Cur'))
        print('-'*40)  
        for i in l:
            print('{:<8}{:<12}{:<20}{:<10}'.format(i['roll_no'],i['name'],i['email'],i['cur']))
    elif ch==3:
        print('{:<8}{:<12}{:<20}{:<10}'.format('Roll_no','Name','Email','Cur'))
        print('-'*40)  
        for i in l:
            print('{:<8}{:<12}{:<20}{:<10}'.format(i['roll_no'],i['name'],i['email'],i['cur']))        
    else:
        print('invalid choice')        
        l.update