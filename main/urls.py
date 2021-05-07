from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.resume, name='resume'),
    path('logout/', views.logoutUser, name='logout'),
    path("create-resume-1/", views.create_resume_1, name="create_resume_1"),
    path("create-resume-2/", views.create_resume_2, name="create_resume_2")
]
