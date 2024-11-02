from django.urls import path
from . import views

app_name = 'private_chats'

urlpatterns = [
    path('main_chats/', views.MyChats.as_view(), name='main_chats'),
    path('main_chats/chat/', views.Chat.as_view(), name='chat'),
    path('main_chats/chat/add_participants_chat/', views.ParticipantsChat.as_view(), name='add_participants_chat'),
    path('main_chats/add_chat/', views.AddChat.as_view(), name='add_chat')
]