from django.urls import path
from .views import car

app_name = 'car'
urlpatterns = [
    path('',car,name='car'),
]