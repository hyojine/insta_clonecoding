from django.db import models
from user.models import User
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="post_pics")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content