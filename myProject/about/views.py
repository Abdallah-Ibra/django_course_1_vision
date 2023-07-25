from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about(request):
    # return HttpResponse('Welcome From About Page!')
    return render(request, 'about.html')
