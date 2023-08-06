"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home
from about.views import about
from blog.views import blog
from car.views import car
from contact.views import contact


urlpatterns = [
    path('',include('home.urls',namespace='home')),
    path('about/',include('about.urls',namespace='about')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('car/',include('car.urls',namespace='car')),
    path('contact/',include('contact.urls',namespace='contact')),
    
    # path('',home,name='home'),
    # path('about/',about,name='about'),
    # path('blog/',blog,name='blog'),
    # path('car/',car,name='car'),
    # path('contact/',contact,name='contact'),
    
    path('admin/', admin.site.urls),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)