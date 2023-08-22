from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
# Create your views here.
def home(request):
    context = {}
    return render(request, "index.html", context)
