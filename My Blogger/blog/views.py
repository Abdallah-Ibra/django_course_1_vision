from django.shortcuts import render

# Create your views here.

def blogs(request):
    context = {}
    return render(request,'blog/blogs.html',context)

def create_blog(request):
    pass

def show_blog(request):
    pass

def edit_blog(request):
    pass

def delete_blog(request):
    pass