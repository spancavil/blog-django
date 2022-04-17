from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=400)
    def __str__(self):
        return (f"User: {self.user}, password: {self.password}")

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=400)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    content = models.CharField(max_length=4000)
    createdAt = models.DateTimeField(auto_now_add=True) #Agrega automáticamente la fecha a la hora de crearse
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (f"id: {self.id}, author: {self.author}, createdAt: {self.createdAt}")
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True) #Agrega automáticamente la fecha a la hora de crearse
    chat = models.CharField(max_length=400)
    def __str__(self):
        return f"id: {self.id}, user: {self.user}, chat: {self.chat}"

    


