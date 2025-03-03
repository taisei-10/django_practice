from django.urls import path
from . import views

app_name='http_server_app'

urlpatterns = [
    path('test', views.index, name='index'),
    path('info', views.info, name='info'),
    path('create', views.create, name='create'),
    path('update/<int:num>', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete')
]