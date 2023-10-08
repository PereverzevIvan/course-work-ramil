from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'beautySalon'

urlpatterns = [
    path('', views.index, name='main'),
    path('user_profile/<int:user_id>', views.show_user_profile, name='user_profile'),
    path('masters/', views.show_all_masters, name='all_masters'),
    path('services/', views.show_all_services, name='all_services'),
    path('one_master/', views.show_one_master, name='show_one_master'),
    path('one_service/', views.show_one_service, name='show_one_service'),
]

handler404 = 'beautySalon.views.error_404'