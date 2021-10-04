from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import  RichTextUploadingField
from product.models import *




class address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    doorno=models.CharField(max_length=100)
    aname=models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    zcode=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    content = RichTextUploadingField(null=True)


    def __str__(self):
        return self.user.username

class mtest(models.Model):
    item=models.CharField(max_length=20)
    price=models.IntegerField()


class payment(models.Model):
    parent=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    method=models.CharField(max_length=100,choices=vchoice,null=True,default="cod")
    cart_product=models.ForeignKey(attributes,null=True,on_delete=models.CASCADE)
    main_product=models.ForeignKey(product,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.parent

vchoice=(
    ("online","online"),
    ("cod","cod"),
)
class payment2(models.Model):
    parent=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    method=models.CharField(max_length=100,choices=vchoice,null=True,default="cod")
    def __str__(self):
        return self.parent


