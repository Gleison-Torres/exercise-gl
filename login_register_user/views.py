from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from . import forms


def index(request):
    return render(request, 'home.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    register = request.session.get('register_form_data')
    return render(request, 'register_user.html', {'forms': forms.RegisterForm(register)})


def register_user_validation(request):
    if not request.POST:
        raise Http404('Página não encontrada!')

    request.session['register_form_data'] = request.POST

    form = forms.RegisterForm(request.POST)
    if form.is_valid():
        save_data = form.save(commit=False)

        user = User.objects.create_user(username=save_data.username, email=save_data.email, password=save_data.password)
        user.first_name = save_data.first_name
        user.last_name = save_data.last_name

        user.save()

        del request.session['register_form_data']
        messages.success(request, 'Usuário cadastrado com sucesso!')

        return redirect('login')
    else:
        return redirect('register')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'login_user.html', {'forms': forms.LoginForm()})


def login_create(request):
    if not request.POST:
        raise Http404('Página não encontrada!')

    form = forms.LoginForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
            return redirect('login')
    else:
        print('Erro no formulário!')
        messages.info(request, 'Algo deu errado, Tente novamente!')
        return redirect('login')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    if str(request.user) == 'AnonymousUser':
        raise Http404('Página não encontrada!')

    return render(request, 'logout_user.html')

