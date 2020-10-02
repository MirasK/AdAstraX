from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

class User(AbstractUser):
    
    class UserType(models.IntegerChoices):
        admin = 1
        teacher = 2
        student = 3

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(blank=True, max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_type = models.PositiveSmallIntegerField(choices = UserType.choices, default = 1)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(default = 0)
    register_date = models.DateTimeField(default=timezone.now, editable = False)


class Teacher(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    students_number = models.IntegerField(default=0)
    lessons_held = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)


class Student(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lessons_passed = models.IntegerField(default=0)
    lessons_left = models.IntegerField(default=0)
    homeworks_passed = models.IntegerField(default=0)


class Admin(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
