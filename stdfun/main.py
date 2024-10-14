from reg_log import *
import user

while True:
    print('''
1.register
2.login
3.exit
''')
    ch=int(input('enter your choice'))
    if ch==1:
        reg()
        
    