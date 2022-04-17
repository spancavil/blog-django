from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    avatar_upload, 
    my_profile,  
    signup, 
    log_in)

urlpatterns = [
    path('profile', my_profile, name="Profile"),
    path('signup', signup, name="Signup"),
    path('login', log_in, name="Login"),
    path('logout', LogoutView.as_view(template_name="accountapp/logout.html"), name="Logout"),
    path('avatar_upload', avatar_upload, name="Avatar"),
]