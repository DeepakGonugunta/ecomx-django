from django.db import models
from product.models import *
from django.contrib.auth.models import User
# Create your models here.
class carousel(models.Model):
    image = models.ImageField(upload_to='pics/')


class history(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    def __str__(self):
        return self.parent

