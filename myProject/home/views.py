from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHi(request):
    return HttpResponse('Hello From First Django App!')

def greet(request,name='Guest'):
    return HttpResponse(f'Welcome Home {name}')

def home(request):
    return HttpResponse('Welcome From Home Page!')