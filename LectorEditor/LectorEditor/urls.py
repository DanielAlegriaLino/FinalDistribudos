"""
URL configuration for LectorEditor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from lector import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="Home" ),
    path('signup/', views.SignUp, name="Signup"),
    path('signin/', views.SignIn, name="Signin"),
    path('logout/', views.LogOut, name='Logout'),
    path('resetpassword/', views.ResetPass, name='Resetpass'),
    path('newpassword/<int:user_id>', views.SetPass, name='Setpass'),
    path('editor/', views.Editor, name="Editor"),
    path('historial/', views.HistorialList, name='Historial'),
]


