from django.urls import path
from . import views

app_name='http_server_app'

urlpatterns = [
    path('test', views.index, name='index'),
]