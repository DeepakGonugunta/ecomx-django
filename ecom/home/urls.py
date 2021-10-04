from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('men/<catt>',views.men),
    path('product/<the_slug>/',views.productdetail),
    path('submit/<the_slug>/',views.productdetail,name="prodetail"),
    path('cart/',views.cartdispaly,name="showcart"),
    path('ajax/',views.ajaxdisplay,name="ajaxcolor"),
    path('addcart/',views.addtocart,name='add'),
    path('delete/',views.cartdelete,name="cartdelete"),
    path('paymentpage/',views.paymen,name="payment"),
    path('checkout',views.checkout,name="checkout"),
    path('myorders/',views.myorders,name="myorders"),
    path('cancellation/',views.cancellation,name="cancellation"),
]
