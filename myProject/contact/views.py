from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse('Hello From Contact Page!')

def test(request):
    return HttpResponse('Hello From Test Contact Page!')
