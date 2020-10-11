from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.index, name='home')
]