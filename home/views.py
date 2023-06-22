from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator


def home_page(request):
    return render(request, 'home.html', {'forms': PasswordResetForm})

