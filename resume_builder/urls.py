from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('main.urls')),
]

# ... the rest of your URLconf goes here ...
