from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from . import forms


def index(request):
    return render(request, 'base.html')


def login_user(request):
    form = forms.LoginForm()
    return render(request, 'login_user.html', {'form': form})


def login_create(request):
    if not request.POST:
        raise Http404('Página não encontrada!')

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user_authenticated = authenticate(
                username=form.cleaned_data['user_customer'],
                password=form.cleaned_data['password_customer']
            )
            if user_authenticated is not None:
                login(request, user_authenticated)
                messages.success(request, 'Logado com sucesso!')
                return redirect('login')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')
                return redirect('login')
        else:
            messages.info(request, 'Formulário inválido!')
            return redirect('login')


def logout_user(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')


def register_user(request):
    return render(request, 'register_user.html')