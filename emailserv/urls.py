from django.urls import path
from emailserv import views
from emailserv.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]