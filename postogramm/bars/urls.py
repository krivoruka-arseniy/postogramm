from django.urls import path
from . import views

app_name = 'bars'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('bar/', views.Bar.as_view(), name='bar'),
    path('bar_chat/', views.BarChat.as_view(), name='bar_chat'),
    path('photo_bar/', views.PhotoBar.as_view(), name='photo_bar'),
    path('add_bar/', views.AddBar.as_view(), name='add_bar'),
    path('add_photo_bar/', views.AddPhotoBar.as_view(), name='add_photo_bar')
]