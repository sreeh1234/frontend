from django.shortcuts import render
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