from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.resume, name='resume'),
    path('logout/', views.logoutUser, name='logout'),
    path("create-resume/", views.create_resume_1, name="create_resume_1"),
    path("create-resume/<str:pk>/",
         views.update_resume, name="update_resume"),

    path("delete-resume/<str:pk>/",
         views.delete_resume, name="delete_resume"),
    path("choose_resume/", views.choose_resume, name="choose_resume"),
    path("choose_template/<str:pk>/",
         views.choose_template, name="choose_template"),

    path("view_template1/<str:pk>/", views.view_template1, name="view_template1"),
    path("print_template1/<str:pk>/", views.print_template1, name="print_template1")
]
