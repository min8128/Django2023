from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('index', views.index, name='index'),
    path('detail/<bpk>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('update/<bpk>', views.update, name='update'),
    path('delete_content/<bpk>', views.delete_content, name='delete_content'),

    path('add_reply/<bpk>', views.add_reply, name='add_reply'),
    path('update_reply/<bpk>/<rpk>', views.update_reply, name='update_reply'),
    path('delete_reply/<bpk>/<rpk>', views.delete_reply, name='delete_reply'),

    path('likey/<bpk>', views.likey, name='likey'),
    path('unlikey/<bpk>', views.unlikey, name='unlikey'),
]