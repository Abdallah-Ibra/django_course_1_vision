from django.shortcuts import render
from .models import Blog, Category
from django.core.paginator import Paginator


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs": page_obj,
    }
    return render(request, "blog/blogs.html", context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {"blog": blog}
    return render(request, "blog/single_blog.html", context)
