from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='next', login_url='login')
def my_profile(request):
    return render(request, 'my_profile.html')


@login_required(redirect_field_name='next', login_url='login')
def my_info(request):
    return render(request, 'my_info.html')


@login_required(redirect_field_name='next', login_url='login')
def my_address(request):
    address = models.AddressUser.objects.filter(user=request.user)
    return render(request, 'my_address.html', {'address': address})


@login_required(redirect_field_name='next', login_url='login')
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
            cep = request.POST.get('postal_code')

            api_link = f'http://viacep.com.br/ws/{cep}/json/'
            info_address = requests.get(api_link)
            address = info_address.json()

            context = {'get_cep': address,
                       'form_add_address': forms.AddressForm,
                       'name': request.POST.get('sender_name')}

            return render(request, 'add_address.html', context)
    else:
        return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})

