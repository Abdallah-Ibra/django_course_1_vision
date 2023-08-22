from django.urls import path
from .views import list_data,create_data,update_data,destroy_data

app_name = 'home'
urlpatterns = [
    path('', list_data, name='list_data'),
    path('create/', create_data, name='create_data'),
    path('edit/<int:pk>', update_data, name='edit_data'),
    path('delete/<int:pk>', destroy_data, name='destroy_data'),
]
