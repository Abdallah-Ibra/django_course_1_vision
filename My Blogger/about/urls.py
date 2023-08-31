from django.urls import path
from .views import about_us

app_name = 'about'
urlpatterns = [
    #  Route|uri
    path('',about_us,name='about')
]

