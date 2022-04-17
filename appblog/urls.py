from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    PostDetail,
    about,
    chat, 
    create_post, 
    inicio, 
    posts_view, 
    search_post, 
    update_post,
    remove_post)

urlpatterns = [
    path('', inicio, name="index"), #Default view
    path('about/', about, name="About"),
    path('pages', posts_view, name="Pages"),
    path('pages/<pk>', PostDetail.as_view(), name="Page detail"),
    path('search-post', search_post, name="Search post"),
    path('create-post', create_post, name="Create post"),
    path('update-post/<id>', update_post, name="Update post"),
    path('remove-post/<id>', remove_post, name="Remove post"),
    path('chat', chat, name="Chat")
]