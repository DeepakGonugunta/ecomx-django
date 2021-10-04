from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/',views.register,name='user_register'),
    path('login/',views.login,name='user_login'),
    path('createuser/',views.create,name='user_create'),
    path('logauth/',views.login_authentication,name='user_auth'),
    path('logout/',views.loggout,name='user_logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('address/',views.addsave),
    path('saddress/',views.showadd),
    path('chart',views.main_view),


]
