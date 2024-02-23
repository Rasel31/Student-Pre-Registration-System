from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        return first_name + ' ' + last_name


class Advisor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        return first_name + ' ' + last_name
