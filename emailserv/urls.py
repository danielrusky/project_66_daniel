from django.urls import path

from emailserv.views import *

urlpatterns = [
    path('', EmailservListView.as_view(), name='list'),
    path('<int:pk>/', EmailservDetailView.as_view(), name='detail'),
    path('create/', EmailservCreateView.as_view(), name='create'),
    path('update/<int:pk>', EmailservUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EmailservDeleteView.as_view(), name='delete'),
    path('create_mail/', MessageCreateView.as_view(), name='create_mail')
]