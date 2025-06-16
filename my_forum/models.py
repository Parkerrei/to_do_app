from django.db import models
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    tasks = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
