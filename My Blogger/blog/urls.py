from django.urls import path
from .views import blog, blog_detail

app_name = "blog"
urlpatterns = [
    path("", blog, name="blog_list"),
    path("<int:pk>", blog_detail, name="blog_detail"),
]
