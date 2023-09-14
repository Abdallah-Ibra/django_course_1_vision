from django.urls import path
from .views import register,user_logout

app_name = "accounts"
urlpatterns = [
    path("signup/", register, name="signup"),
    path("logout/", user_logout, name="logout"),
]
