from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from .models import Bars, ImgBar, FavoriteBar, BarMessages
from .forms import AddMessage, AddBarsForm, AddPhotoBarForm
from django.urls import reverse, reverse_lazy
from users.models import Users


class Main(View):
    def get(self, request):
        bars = Bars.objects.filter(public=True)
        
        return render(request, 'bars/main.html', {'bars': bars})
    
    def post(self, request):
        bars = Bars.objects.filter(public=True)
        button = request.POST['button']
        if button == 'filter':
            bar_cat = request.POST['bar_category']
            if bar_cat == 'all':
                pass
            else:
                bars = Bars.objects.filter(bar_category=bar_cat)
        else:
            request.session['pk_bar'] = button
            return redirect('bar/')
        
        return render(request, 'bars/main.html', {'bars': bars})

    
class Bar(View):
    def get(self, request):
        pk_bar = request.session['pk_bar']
        bar = Bars.objects.get(pk=pk_bar)
        
        return render(request, 'bars/bar.html', {'bar': bar})
    
    def post(self, request):
        pk_bar = request.session['pk_bar']
        bar = Bars.objects.get(pk=pk_bar)
        user_pk = self.request.user.pk
        user = Users.objects.get(pk=user_pk)
        if user.user_status_id == 3 or user_pk == bar.owner_bar_id:
            bar.public = False
            bar.save()    
        else:
            pass
        
        return render(request, 'bars/bar.html', {'bar': bar})
    
    
class PhotoBar(ListView):
    model = ImgBar
    template_name = 'bars/photo_bar.html'
    context_object_name = 'photo_bar'
    
    def get_queryset(self):
        pk_bar = self.request.session['pk_bar']
        photo_bar = ImgBar.objects.filter(where_img=pk_bar)
        return photo_bar
    
    
class BarChat(View):
    def get(self, request):
        form = AddMessage
        pk_bar = request.session['pk_bar']
        bar_message = BarMessages.objects.filter(where_message=pk_bar)
        
        return render(request, 'bars/bar_message.html', {'form': form, 'bar_message': bar_message})
    
    def post(self, request):
        form = AddMessage
        pk_bar = request.session['pk_bar']
        bar_message = BarMessages.objects.filter(where_message=pk_bar)
        button = request.POST['button']
        if button == 'add_message':
            BarMessages.objects.create(
                where_message_id=pk_bar,
                owner_message_id=self.request.user.pk,
                name=request.POST['name'],
                content = request.POST['content']
            )
        else:
            message = BarMessages.objects.get(pk=button)
            if message.owner_message_id == self.request.user.pk:
                message.delete()
            else:
                pass
        
        return render(request, 'bars/bar_message.html', {'form': form, 'bar_message': bar_message})
    
    
class AddBar(CreateView):
    template_name = 'bars/add_bar.html'
    form_class = AddBarsForm
    success_url=reverse_lazy('bars:main')
    
    def form_valid(self, form):
        try:
            user_pk = self.request.user.pk
            user = Users.objects.get(pk=user_pk)
            if user.user_status_id == 2 or user.user_status_id == 3:
                valid_f = form.save(commit=False)
                valid_f.owner_bar_id = user_pk
            else:
                pass
        except:
            pass
        return super().form_valid(form)
    
    
class AddPhotoBar(CreateView):
    template_name = 'bars/add_photo_bar.html'
    form_class = AddPhotoBarForm
    success_url=reverse_lazy('users:profile')
    
    def form_valid(self, form):
        f_valid = form.save(commit=False)
        f_valid.where_img_id=self.request.session['pk_bar']
        return super().form_valid(form)