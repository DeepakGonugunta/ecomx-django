from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import  RichTextUploadingField



# Create your models here.
class category(models.Model):
    parent_category = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='pics/')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


vchoice=(
    ("yes","y"),
    ("no","n"),
)
class size_variant(models.Model):
    size=models.CharField(max_length=30)
    def __str__(self):
        return self.size


class color_variant(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.name

    
vvchoice=(
    ("yes","yes"),
    ("no","no"),
)
class product(models.Model):
   parent_category = models.ForeignKey(category, on_delete=models.CASCADE)
   title = models.CharField(max_length=150)
   description=models.TextField(max_length=500)
   price=models.CharField(max_length=30)
   slug=models.SlugField()
   image=models.ImageField(blank=True,upload_to='pics/')
   des=models.CharField(max_length=30,choices=vchoice,default="y")
   size=models.ForeignKey(size_variant,null=True,on_delete=models.SET_NULL)
   color=models.ForeignKey(color_variant,blank=True,null=True,on_delete=models.SET_NULL)
   content = RichTextUploadingField(null=True)
   check=models.CharField(max_length=20)

    

   def __str__(self):
        return self.title




   def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""    



class images(models.Model):
    img_product=models.ForeignKey(product,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    image=models.ImageField(blank=True,upload_to='pics/')

    def __str__(self):
        return self.title







class attributes(models.Model):
    parent_category = models.ForeignKey(category,null=True, on_delete=models.CASCADE)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    size=models.ForeignKey(size_variant,null=True,on_delete=models.SET_NULL)
    color=models.ForeignKey(color_variant,null=True,on_delete=models.SET_NULL)
    price=models.IntegerField()
    image=models.ImageField(blank=True,upload_to='pics/')
    check=models.CharField(max_length=20)
    content = RichTextUploadingField(null=True)

    def __str__(self):
        return self.product.title


class img_attributes(models.Model):
    product=models.ForeignKey(attributes, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='pics/')
    def __str__(self):
        return self.product.product.title



class cart(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    cart_product=models.ForeignKey(attributes,null=True,on_delete=models.CASCADE)
    main_product=models.ForeignKey(product,null=True,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,default=None,blank=True)
    title=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

class rec(models.Model):
    main=models.ForeignKey(product,null=True,on_delete=models.CASCADE,related_name="main")
    rec1=models.ForeignKey(product,null=True,on_delete=models.CASCADE,related_name="rec1")
    rec2=models.ForeignKey(product,null=True,on_delete=models.CASCADE,related_name="rec2",blank=True)