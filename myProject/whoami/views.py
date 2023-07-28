from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def whoami(request):
    return HttpResponse('This Just Funny Page!')


def hoppies(request):
    return HttpResponse('I Love Play Piano!')