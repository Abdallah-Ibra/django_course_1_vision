from django.urls import path
from about.views import about,test

urlpatterns = [
    path('',about),
    path('test/',test)
]
