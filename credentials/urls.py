from . import views
from django.urls import path

urlpatterns = [
    path('register', views.reg, name='registration'),
    path('login', views.log, name='login'),
    path('logout', views.out, name='logout')
]