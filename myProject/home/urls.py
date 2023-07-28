from django.urls import path
from home.views import home,sayHi
# from  .views import home


urlpatterns = [
    path('',home),
    path('hi/',sayHi)
]


# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/home/hi