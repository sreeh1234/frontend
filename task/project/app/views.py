from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("welcome to all")

def fun2(request,salary,year):
    if year>5:
        salary='bonus is ',0.05*salary
    else:
        salary='no bonus'
     
    return HttpResponse(salary,year)


def fun3(request,num):
    num=num%100
    if num%3==0:
        num='it is divisible by 3'
    else:
        num='not divisible by 3'
    return HttpResponse(num)

def fun4(request,unit):
    if unit<=100:
        print("no charge")  
    elif 100<unit<=200:
        unit=(unit-100)*5
    else:
        unit=500+(unit-200)*10
    return HttpResponse(unit)



def fun5(request,city):
    
    if city=='delhi':
        city="RedFort"
    elif city=='agra':
        city="TajMahal" 
    elif city=='jaipur':
        city="JalMahal"         
    else:
        city="invalid entry"    

    return HttpResponse(city)


def fun6(request,num):
    
    
    if num==1:
        num="SUNDAY"
    elif num==2:
        num="MONDAY"
    elif num==3:
        num="TUESDAY"
    elif num==4:
        num="WEDNESDAY"
    elif num==5:
        num="THURSDAY" 
    elif num==6:
        num="FRIDAY"
    elif num==7:
        num="SATURDAY"
    else:
        num="invalid"    

    return HttpResponse(num)


def fun7(request,cost):
    if cost<=50000:
        cost=0.05*cost
    elif 50000<cost<=100000:
        cost=0.1*cost
    else:
        cost=tax=0.15*cost  
    return HttpResponse(cost)

def fun8(request):
    a={'name':'anu','age':22}
    b=20
    c=[1,2,3]
    d=[{'name':'sanju','age':12},{'name':'anju','age':22}]
    return render(request,'demo.html',{'data':a,'b':b,'c':c,'d':d})

def fun9(req):
    a={'name':'anju','age':29},{'name':'sanju','age':25},{'name':'ron','age':42},{'name':'don','age':30}
    
    l1=[]
    l2=[]
    for i in a:
        if i['age']>=30:
            l1.append(i)
        else:
            l2.append(i)    
    return render(req,'demo.html',{'a':a,'l1':l1,'l2':l2})


std=[{'roll_no':'1','name':'sanju','age':25},{'roll_no':'2','name':'anju','age':23}]
def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'roll_no':roll,'name':name,'age':age})
        print(std)
        return redirect(add_std)
    else:
        return render(req,'add_std.html',{'std':std})   
    
    
def edit_std(req,id):
    print(id)
    student=''
    for i in std:
        if i['roll_no']==id:
            student=i
    print(student)
    if req.method=='POST':  
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']   
        student['roll_no']=roll     
        student['name']=name
        student['age']=age
        return redirect(add_std)
    else:
        return render(req,'edit.html',{'data':student})
    
def delete_std(req,id):
    for i in std:
        if i['roll_no']==id:
            std.remove(i)
            return redirect(add_std)    