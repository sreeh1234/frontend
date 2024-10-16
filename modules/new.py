# lim=int(input('enter limit'))
# f=open('demo.txt','w')
# for i in range (lim):
#     name=input('enter name')
#     f.write(name+'\n')


num=int(input('enter a  number : '))
f=open('demo.txt','w')
for i in range (1,11):
    print(i,'*',num,'=',i*num)
    f.write(str(i)+'*'+str(num)+'='+str(i*num)+'\n')
    