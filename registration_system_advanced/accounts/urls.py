from django.urls import path
from .views import register

app_name = 'accounts'
urlpatterns = [
    path('signup/',register,name='register')
]
