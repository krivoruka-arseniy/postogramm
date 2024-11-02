from django import forms
from .models import PrivateMessages, PrivateChat


class AddMessage(forms.ModelForm):
    class Meta:
        model = PrivateMessages
        fields = [
            'name',
            'content'
        ]
        
        
class AddChatForm(forms.ModelForm):
    class Meta:
        model = PrivateChat
        fields = ['name']
        
        
class AddParticipants(forms.Form):
    name = forms.CharField(max_length=20)