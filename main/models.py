from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserTag(models.Model):
    userType = models.CharField(max_length=35, null=True, blank=True)
    maxPost = models.IntegerField(null=True, blank=True)
    canEdit = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.userType}'


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blogTitle = models.CharField(max_length=35, blank=True, null=True)
    blogContent = models.TextField(null=True, blank=True)
    isApproved = models.BooleanField(default=False)
    dateModified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.blogTitle}'


class Blogger(models.Model):
    blogUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userType =  models.ForeignKey(UserTag, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.blogUser.username}'


class SupervisorReqs(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, null=True)
    isSupervisor = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.blogger.blogUser.username}'