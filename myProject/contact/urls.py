from django.urls import path
from contact.views import contact,test

urlpatterns = [
    path('',contact),
    path('test/',test),
]