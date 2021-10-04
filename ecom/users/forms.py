from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms  import UserCreationForm
from django.forms.widgets import Input
from .import models



class register_user(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
             "password1": Input(attrs={
                "type":"password",
                "class":"form-control my-3 p-4",
                "placeholder":"password",
            }),
            "password2": Input(attrs={
                "type":"password",
                "class":"form-control my-3 p-4",
                "placeholder":"confirm password",
            }),
            "username":Input(attrs={
                "type":"text",
                "class":"form-control my-3 p-4",
                "placeholder":"username",
            }),
             "email":Input(attrs={
                "type":"email",
                "class":"form-control my-3 p-4",
                "placeholder":"email",
            }),
            

            
        }


class login_user(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
             "password": Input(attrs={
                "type":"password",
                "class":"form-control my-3 p-4",
                "placeholder":"********",
            }),
            "username":Input(attrs={
                "type":"text",
                "class":"form-control my-3 p-4",
                "placeholder":"username",
            }),
            

            
        }

class aform(ModelForm):
    class Meta:
        model=models.address
        fields='__all__'