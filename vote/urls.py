from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('index/', views.index, name='index'),

    path('detail/<vpk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('vote/<vpk>', views.vote, name='vote'),

    path('delete/<vpk>', views.delete, name='delete'),
    path('cancel/<vpk>', views.cancel, name='cancel')
]