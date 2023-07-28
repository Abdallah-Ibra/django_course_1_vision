from django.urls import path
from whoami.views import whoami,hoppies

urlpatterns = [
    path('',whoami),
    path('hoppies/',hoppies),
]
