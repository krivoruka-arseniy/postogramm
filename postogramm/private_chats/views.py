from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from .models import PrivateChat, PrivateMessages
from .forms import AddMessage, AddChatForm, AddParticipants
from users.models import Users


class MyChats(View):
    def get(self, request):
        user_pk = self.request.user.pk
        user_chats = PrivateChat.objects.filter(users=user_pk)
        
        return render(request, 'private_chats/main_chats.html', {'user_chats': user_chats})
    
    def post(self, request):
        chat_pk = request.POST['button']
        request.session['chat_pk'] = chat_pk
        
        return redirect('private_chats:chat')
    
    
class Chat(View):
    def get(self, request):
        form = AddMessage
        chat_pk = request.session['chat_pk'] 
        messages = PrivateMessages.objects.filter(where_message=chat_pk)
        
        return render(request, 'private_chats/chat.html', {'form': form, 'messages': messages})

    def post(self, request):
        form = AddMessage
        chat_pk = request.session['chat_pk'] 
        messages = PrivateMessages.objects.filter(where_message=chat_pk)
        button = request.POST['button']
        user_pk = self.request.user.pk
        if button == 'delete_chat':
            chat = PrivateChat.objects.get(pk=chat_pk)
            if user_pk == chat.owner_chat_id:
                chat.delete()
            else:
                pass
        elif button == 'add_message':
            PrivateMessages.objects.create(
                owner_message_id=user_pk,
                where_message_id=chat_pk,
                name=request.POST['name'],
                content=request.POST['content']
            )
        else:
            message = PrivateMessages.objects.get(pk=button)
            if user_pk == message.owner_message_id:
                message.delete()
            else:
                pass

        return render(request, 'private_chats/chat.html', {'form': form, 'messages': messages})
    
    
class ParticipantsChat(View):
    def get(self, request):
        chat_pk = request.session['chat_pk'] 
        chat = PrivateChat.objects.get(pk=chat_pk)
        form = AddParticipants
        
        return render(request, 'private_chats/add_participants_chat.html', {'chat': chat, 'form': form})
    
    def post(self, request):
        chat_pk = request.session['chat_pk'] 
        chat = PrivateChat.objects.get(pk=chat_pk)
        form = AddParticipants
        button = request.POST['button']
        if button == 'add_user':
            name = request.POST['name']
            user = Users.objects.get(username=name)
            chat.users.add(user.pk)
        else:
            if self.request.user.pk == chat.owner_chat_id:
                chat.users.remove(button)
            else:
                pass
        
        return render(request, 'private_chats/add_participants_chat.html', {'chat': chat, 'form': form})
    
    
class AddChat(View):
    def get(self, request):
        form = AddChatForm
        status = ''
        
        return render(request, 'private_chats/add_chat.html', {'form': form, 'status': status})
    
    def post(self, request):
        try:
            form = AddChatForm
            user_pk = self.request.user.pk
            chat = PrivateChat.objects.create(
                owner_chat_id=user_pk,
                name=request.POST['name']
            )
            chat.users.add(user_pk)
            status = ''
        except:
            status = 'необходимо зарегистрироватся'
        
        return render(request, 'private_chats/add_chat.html', {'form': form, 'status': status})