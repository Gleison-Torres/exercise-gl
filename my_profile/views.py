from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib import messages
from pycep_correios import get_address_from_cep, WebService


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
            address = get_address_from_cep(request.POST.get('postal_code'), webservice=WebService.APICEP)

            context = {'get_cep': address,
                       'form_add_address': forms.AddressForm,
                       'name': request.POST.get('sender_name')}

            return render(request, 'add_address.html', context)
    else:
        return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})


def get_cep(request):
    cep = request.POST.get('postal_code')
    print(cep)
    return redirect('')