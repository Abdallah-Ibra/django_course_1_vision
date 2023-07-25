
from home.views import *
from django.urls import path

urlpatterns = [
    path('',showHome,name='home'),
    path('sayHi/',sayHi,name='sayHi'),
    path('greet/',greet,name='greet'),
]