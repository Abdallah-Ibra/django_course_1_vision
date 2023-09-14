from django.urls import path
from .views import blog, blog_detail,category_show

app_name = "blog"
urlpatterns = [
    path("", blog, name="blog_list"),
    path("<slug:slug>", blog_detail, name="blog_detail"),
    path("categories/<int:pk>", category_show, name="category_show"),
]
