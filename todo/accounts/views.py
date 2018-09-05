from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponse('Usuário gravado!')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('core')
        else:
            messages.error(request, 'Usuário ou senha inválido.')

    return render(request, 'accounts/user_login.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com Sucesso!')
            return redirect('change_password')
        else:
            messages.error(request, 'Erro ao alterar senha!')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('login_user')

