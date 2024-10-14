import add
import sub
import mul
import div
from numbers import num

while True:
    print('''
1.add
2.sub
3.mul
4.div
5.exit
''')
    ch=int(input('enter your choice'))
    if ch==1:
        a,b=num()
        add.add(a,b)
    elif ch==2:
        a,b=num()
        sub.sub(a,b)   
    elif ch==3:
        a,b=num()
        mul.mul(a,b)  
    elif ch==4:
        a,b=num()
        div.div(a,b) 
    elif ch==5:
        break            