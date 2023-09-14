from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")
        else:
            form = RegisterForm()

        context = {"form": form}
        return render(request, "registration/register.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect("/")
