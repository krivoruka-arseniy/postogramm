from django.shortcuts import render, redirect
from django.views import View
from .models import Users
from bars.models import Bars
from .forms import RegisterUser
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


def RegisterUsers(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password1'])
            user.save()
            status = 'Вы успешно зарегистрированы, теперь необходимо войти в аккаунт'
        else:
            status = 'что то пошло не так :('

    else:
        form = RegisterUser()
        status = ''
    
    return render(request, 'users/register.html', {'form': form, 'status': status})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('bars:main')


class Profile(View):
    def get(self, request):
        u = self.request.user.pk
        user = Users.objects.get(pk=u)
        user_bars = Bars.objects.filter(owner_bar=u)
        status = ''
        
        return render(request, 'users/profile.html', {'user': user, 'user_bars': user_bars, 'status': status})
    
    def post(self, request):
        try:
            u = self.request.user.pk
            user = Users.objects.get(pk=u)
            user_bars = Bars.objects.filter(owner_bar=u)
            pk_bar = request.POST['pk_bar']
            action_bar = request.POST['action_bar']
            if action_bar == 'delete':
                Bars.objects.get(pk=pk_bar).img.delete(save=True)
                Bars.objects.get(pk=pk_bar).delete()
            else:
                request.session['pk_bar'] = pk_bar
                return redirect('bars:add_photo_bar')
            status = ''
        except:
            status = 'необходимо зарегистрироватся'
        
        return render(request, 'users/profile.html', {'user': user, 'user_bars': user_bars, 'status': status})