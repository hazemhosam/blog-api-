from django.db import models
from django.conf import settings 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    auther = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts') 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title 


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comments') 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_comments') 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content 

