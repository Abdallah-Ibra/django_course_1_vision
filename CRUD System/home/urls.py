from django.urls import path
from .views import list_data,add_data,edit_data,destroy_data

app_name = 'home'
urlpatterns = [
    path('',list_data,name='list_data'),
    path('add/',add_data,name='add_data'),
    path('edit/<int:pk>',edit_data,name='edit_data'),
    path('delete/<int:pk>', destroy_data,name='destroy_data'),  
]
