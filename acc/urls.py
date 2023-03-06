from django.urls import path
from . import views

app_name = 'acc'

urlpatterns = [
    path('index/', views.index, name='index'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user_delete/', views.user_delete, name="user_delete"),

    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('chpass/', views.chpass, name='chpass'),
]