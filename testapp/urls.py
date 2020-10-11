from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.image_upload_view, name='image_upload_view')
    
]