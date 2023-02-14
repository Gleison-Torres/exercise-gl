from django.shortcuts import render
from . import models
from . import forms
from django.http import Http404


def my_profile(request):
    return render(request, 'my_profile.html')


def my_info(request):
    return render(request, 'my_info.html')


def my_address(request):
    address = models.AddressUser.objects.filter(user=request.user)
    return render(request, 'my_address.html', {'address': address})


def add_address(request):
    if request.method != 'POST':
        raise Http404('Página não encontrada!')

    return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})
