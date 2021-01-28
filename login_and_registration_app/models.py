from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name is too short"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name is too short"
        if len(postData['password']) < 8:
            errors['lenpas'] = "Password is too short"
        if postData['password'] != postData['conpass']:
            errors['password'] = "Confirm password did not match"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        user = User.objects.filter(email = postData['email'])
        if user:
            errors['exists'] = "Email already exists"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
# Create your models here.
