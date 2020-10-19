from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

# adastra123
adastra = 'pbkdf2_sha256$180000$V0u9CLVr79Oa$EwlNZ4A64fEIAXKRXcltAuhmJJYZF7HXsgoy86DLQcE='


class UserType(models.IntegerChoices):
    admin = 1
    teacher = 2
    student = 3


class User(AbstractUser):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100, blank = True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default = adastra)
    user_type = models.PositiveSmallIntegerField(choices = UserType.choices, default = 1)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length = 20,blank = True)
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


class TitleType(models.TextChoices):
    Math = 'Math'
    Physics = 'Physics'
    English = 'English'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(choices = TitleType.choices)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default= 1)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, default= 1)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    allDay = models.BooleanField(default=False)

    def __str__(self):
        return self.title
