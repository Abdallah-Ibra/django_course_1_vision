from django.urls import path
from team.views import team


app_name = 'team'
urlpatterns = [
    path('',team,name = 'team')
]