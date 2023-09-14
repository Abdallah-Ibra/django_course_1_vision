from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Blog, Category,Comment,Like
from django.core.paginator import Paginator
from .forms import CommentForm
from .filters import BlogFilter

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    
    # filters
    myfilter = BlogFilter(request.GET,queryset=blogs)
    blogs = myfilter.qs
    
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "blogs": page_obj,
        'myfilter':myfilter
    }
    return render(request, "blog/blogs.html", context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog).all()
    total_comments = Comment.objects.filter(blog=blog).count()
    total_likes = Like.objects.filter(blog=blog).count()
    categories = Category.objects.all()
    recent_blogs = Blog.objects.all().order_by('-created_at')[:4]
    
    comment_form = CommentForm(request.POST or None)
    # if request.method == 'POST':
    #     if comment_form.is_valid():
    #         if request.user.is_authenticated:
    #             # print(comment_form.cleaned_data['first_name'])
    #             # print(comment_form.cleaned_data['last_name'])
    #             # print(comment_form.cleaned_data['email'])
    #             # print(comment_form.cleaned_data['text'])
    #             save_form = comment_form.save(commit=False)
    #             save_form.first_name = request.user.first_name if request.user.first_name != '' else 'First Name'
    #             save_form.last_name = request.user.last_name if request.user.last_name != '' else 'Last Name'
    #             save_form.email = request.user.email if request.user.email != '' else 'email@email.com'
    #             save_form.blog = blog
    #             save_form.save()
    #             return redirect(reverse('blog:blog_detail',kwargs={'slug':slug}))
    #         else:
    #             save_form = comment_form.save(commit=False)
    #             save_form.blog = blog
    #             save_form.save()
    #             return redirect(reverse('blog:blog_detail',kwargs={'slug':slug}))
    #     else:
    #         comment_form = CommentForm(request.POST or None)
    #         return redirect(reverse('blog:blog_detail',kwargs={'slug':slug}))
    
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if fname and lname and email and message:
            if request.user.is_authenticated:
                img = request.user.profile.image
                ccomment = Comment(first_name=fname,last_name=lname,email=email,text=message,blog=blog,image=img)
            else:
                ccomment = Comment(first_name=fname,last_name=lname,email=email,text=message,blog=blog)
                
            ccomment.save()
        return redirect(reverse('blog:blog_detail',kwargs={'slug':slug}))
    
    context = {
        "blog": blog,
        'comments':comments,
        'total_comments':total_comments,
        'total_likes':total_likes,
        'categories':categories,
        'comment_form': comment_form,
        'recent_blogs':recent_blogs
        }
    return render(request, "blog/single_blog.html", context)


def category_show(request,pk):
    category = Category.objects.get(pk=pk)
    category_blogs = category.category_blogs.all()
    paginator = Paginator(category_blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'category':category,
        'category_blogs':page_obj,
    }
    return render(request,'blog/category_show.html',context)


# def create_blog(request):
#     pass

# def edit_blog(request):
#     pass

# def delete_blog(request):
#     pass