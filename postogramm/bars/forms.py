from django import forms
from .models import BarMessages, Bars, ImgBar


class AddMessage(forms.ModelForm):
    class Meta:
        model = BarMessages
        fields = [
            'name',
            'content'
        ]
        
        
class AddBarsForm(forms.ModelForm):
    class Meta:
        model = Bars
        fields = [
            'img',
            'name',
            'description',
            'bar_category'
        ]
        
        
class AddPhotoBarForm(forms.ModelForm):
    class Meta:
        model = ImgBar
        fields = [
            'img',
            'name_img'
        ]