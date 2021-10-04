from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','parent_category']


class ProductImage(admin.TabularInline):
    model=images
    extra=5   


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','parent_category']   
    inlines=[ProductImage] 



class attImage(admin.TabularInline):
    model=img_attributes
    extra=5 
  
class attAdmin(admin.ModelAdmin):
    inlines=[attImage] 


  

admin.site.register(img_attributes)

admin.site.register(category,CategoryAdmin)
admin.site.register(product,ProductAdmin)
admin.site.register(images)
admin.site.register(cart)
admin.site.register(attributes,attAdmin)
admin.site.register(color_variant)
admin.site.register(size_variant)






# Register your models here.
