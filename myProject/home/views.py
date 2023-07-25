from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHi(request):
    return HttpResponse('Say Hi')


def greet(request,name:str):
    return HttpResponse(f'<h1>Hello  {name.title()}</h1>')


def showHome(request):
    names = ['Abdallah','Eman','Amir','Yusuf','Malik','Ali','Ahmed']
    context = {
        'names':names
    }
    return render(request,'home.html',context=context)