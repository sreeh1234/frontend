from django.shortcuts import render

# Create your views here.
def fun1(req):
    return render(req,'index.html')

def fun2(req):
    return render(req,'about.html')

def fun3(req):
    return render(req,'book.html')

def fun4(req):
    return render(req,'menu.html')