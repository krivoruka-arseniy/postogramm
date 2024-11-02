from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
    path('register/', views.RegisterUsers, name='register'),
    path('register/login/', views.LoginUser.as_view(), name='login')
]