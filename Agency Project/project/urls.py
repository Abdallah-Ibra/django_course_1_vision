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
from home.views import home
from about.views import about
from portfolio.views import portfolio
from team.views import team
from contact.views import contact
from services.views import services

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('about/',include('about.urls',namespace='about')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('portfolio/',include('portfolio.urls',namespace='portfolio')),
    path('services/',include('services.urls',namespace='services')),
    path('team/',include('team.urls',namespace='team')),
    # path('about/',about,name= 'about'),
    # path('contact/',contact,name= 'contact_us'),
    # path('portfolio/',portfolio,name= 'portfolio'),
    # path('services/',services,name= 'services'),
    # path('team/',team,name= 'team'),
    path('admin/', admin.site.urls),
    
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
