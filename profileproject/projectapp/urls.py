from django.urls import path

from projectapp import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_fun, name='log'),
    path('logdata', views.profile, name='profile'),
    path('home',views.home,name = 'home'),
    path('email',views.email,name = 'email'),
    path('contact',views.contact,name = 'contact'),

]
