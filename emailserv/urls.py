from django.urls import path
from emailserv import views

urlpatterns = [
    path('', views.home, name='home'),
]