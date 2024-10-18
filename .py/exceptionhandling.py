# try:
#     print('10'+'abc')
#     print('no error')
    
# except:
    
#     print('hello')  
#     print('hello')  


l=[1,2.5,'ad',6,9,6]
sum=0
for i in l:
    try:
        sum+=i
    except:
        pass
    print(sum)

            