"""disney URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('signup',views.signupview,name='signup'),
    path('login',views.loginview,name='login'),
    path('subs',views.subspage,name='subscrip'),
    path('home',views.home,name='home'),
    path('moviespg',views.moviedesc,name='moviespg'),
    path('',views.user,name='user'),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
