"""
URL configuration for merch_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from .views import loginview,logoutview,signupview,welcomeview,profileview,profile_editview,profile_address,pass_changeview

urlpatterns = [
    path("login/", loginview, name="login" ),
    path('logout/', logoutview , name = 'logout'),
    path("register/", signupview, name="register"),
    path("welcome/", welcomeview, name="welcome"),
    path("profile/", profileview, name="profile"),
    path("profile/edit/", profile_editview , name="profile_edit"),
    path("profile/address/", profile_address , name="profile_address"),
    path("profile/password-change/", pass_changeview , name="pass_change"),
]
