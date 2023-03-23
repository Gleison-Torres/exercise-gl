from django.shortcuts import render, redirect
from . import models
from login_register_user.models import DataUser
from . import forms
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='next', login_url='login')
def my_profile(request):
    return render(request, 'my_profile.html')


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
            return render(request, 'add_address.html')

    return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})


def delete_address(request, pk):
    if request.method == 'GET':
        raise Http404('Página não encontrada!')

    address = models.AddressUser.objects.get(id=pk)
    address.delete()
    messages.success(request, 'O endereço foi excluído com sucesso!')
    return redirect('address')


@login_required(redirect_field_name='next', login_url='login')
def edit_address(request, pk):
    address = models.AddressUser.objects.get(id=pk, user=request.user)
    form = forms.AddressForm(request.POST or None, instance=address)

    context = {
        'address': address,
        'form': form
    }

    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'Endereço alterado com sucesso!')
            return redirect('address')
        else:
            messages.info(request, 'Algo deu errado, tente novamente!')

    return render(request, 'edit_address.html', context)


@login_required(redirect_field_name='next', login_url='login')
def my_info(request):

    context = {
        'user_info': DataUser.objects.get(user_profile=request.user),
        'address': models.AddressUser.objects.get(user=request.user, active=True)
    }

    return render(request, 'my_info.html', context)

