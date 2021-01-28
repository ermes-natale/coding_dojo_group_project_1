from django.db import models
from login_and_registration_app.models import User
# import re

class PostManager(models.Manager):
    def validate_post(self, postData):
        errors = {}
        if len(postData['text']) < 1:
            errors['text'] = "Content required"

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=144)
    likes = models.IntegerField()
    author = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = PostManager()