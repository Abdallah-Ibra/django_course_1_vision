from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        acceptCondtions = request.POST.get("accept_conditions")

        print("-" * 50)
        print(f"[+] USER: {username}")
        print(f"[+] EMAIL: {email}")
        print(f"[+] PASS1: {pass1}")
        print(f"[+] PASS2: {pass2}")
        print(f"[+] Accept: {acceptCondtions}")
        print("-" * 50)

        if username and email and pass1 and pass2 and acceptCondtions:
            newUser = User.objects.create_user(username, email, pass1)
            newUser.save()
            messages.success(request, "Account Created Successfully")
            return redirect("login")
        elif pass1 != pass2:
            messages.error(request, "Passwords Don't Match!")
        else:
            messages.warning(
                request, "Invalid Credentials, Please Fill True Data and Try Again!"
            )

    context = {}
    return render(request, "signup.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("-" * 50)
        print(f"[+] USER: {username}")
        print(f"[+] Password: {password}")
        print("-" * 50)

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid Username or Password!")
        else:
            messages.warning(
                request, "Invalid Credentials, Please Fill True Data and Try Again!"
            )

    context = {}
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("login")
