
from django.urls import path
from . import views

urlpatterns = [
     path('register',views.registration ),
    path('login',views.my_login),
    path('',views.home),
]







 











