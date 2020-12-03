from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    MARK = (
        ('all','all'),
        ('managers','managers'),
        ('middle','middle'),
        ('secret','secret'),
        ('top secret','top secret')
    )

    name = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    mark = models.CharField(max_length=100,choices=MARK)

    def __str__(self):
        return self.name


class Account(models.Model):
    ROLE = (
        ('no rights','no rights'),
        ('Cleaner','Cleaner'),
        ('Manager','Manager'),
        ('System Admin','System Admin'),
        ('General Director','General Director'),
        ('Master','Master')
    )

    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120,choices=ROLE,default='no rights')
    phone = models.IntegerField()

    def __str__(self):
        return self.last_name





