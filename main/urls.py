from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('resume/', views.resume, name='resume'),
    path('logout/', views.logoutUser, name='logout'),
    path("create-resume/", views.create_resume, name="create_resume"),
]
