from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('finish/<tpk>', views.finish, name='finish'),
    path('delete/<tpk>', views.delete, name='delete'),
]