from django.contrib import admin
from .models import Avatar, Chat, Usuario, Post

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Avatar)
admin.site.register(Chat)