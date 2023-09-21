from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from . import forms, models

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse


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
        # Cria conta  (Nome, Sobrenome, usuário, E-mail e senha).

        user_account = User.objects.create_user(
            username=save_data.username,
            email=save_data.email,
            password=save_data.password,
            is_active=False
        )

        user_account.first_name = save_data.first_name
        user_account.last_name = save_data.last_name
        user_account.save()

        # Cria perfil (CPF e telefone).
        models.DataUser.objects.create(
            user_profile=user_account, cell_phone=form.cleaned_data.get('cell_phone'), cpf=form.cleaned_data.get('cpf')
        )

        # Geração de token e envio de email para confirmação de conta.
        current_site = get_current_site(request)

        mail_subject = 'Confirme sua conta na The Whipper Games'

        message = render_to_string('acc_active_email.html', {
            'user': save_data,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user_account.pk)),
            'token': account_activation_token.make_token(user_account)
        })

        to_email = form.cleaned_data.get('email')

        email = EmailMessage(
            subject=mail_subject,
            body=message,
            to=[to_email]
        )

        email.send()

        # Remove as informações salvas na session e confirma que email foi enviado.

        del request.session['register_form_data']
        messages.success(request, 'Por favor cheque seu email para ativar sua conta.')

        return redirect('login')
    else:
        return redirect('register')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


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
            messages.success(request, f'Você está logado com o usuário "{request.user}"')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
            return redirect('login')
    else:
        messages.info(request, 'Algo deu errado, Tente novamente!')
        return redirect('login')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    if str(request.user) == 'AnonymousUser':
        raise Http404('Página não encontrada!')

    return render(request, 'logout_user.html')
