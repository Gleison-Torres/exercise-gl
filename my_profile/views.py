from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib import messages


def my_profile(request):
    return render(request, 'my_profile.html')


def my_info(request):
    return render(request, 'my_info.html')


def my_address(request):
    address = models.AddressUser.objects.filter(user=request.user)
    return render(request, 'my_address.html', {'address': address})


def add_address(request):
    if request.method == 'POST':
        form_add_address = forms.AddressForm(request.POST)
        if form_add_address.is_valid():
            pre_save_address = form_add_address.save(commit=False)
            pre_save_address.user = request.user
            pre_save_address.save()
            messages.success(request, 'Endereço cadastrado com sucesso!')
            return redirect('address')
        else:
            messages.error(request, 'Erro no preenchimento do formulário!')
            return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})
    else:
        return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})
