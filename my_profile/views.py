from django.shortcuts import render, redirect
from . import models, forms
from login_register_user.models import DataUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import Http404


@login_required(login_url='login')
def my_profile(request):
    return render(request, 'my_profile.html')


@login_required(login_url='login')
def my_address(request):

    context = {
        'active_address': models.AddressUser.objects.filter(user=request.user, active=True),
        'other_address': models.AddressUser.objects.filter(user=request.user, active=False)
    }

    return render(request, 'my_address.html', context)


@login_required(login_url='login')
def add_address(request):
    if request.method == 'POST':
        form_add_address = forms.AddressForm(request.POST)
        if form_add_address.is_valid():
            print('formulario valido')
            pre_save_address = form_add_address.save(commit=False)
            pre_save_address.user = request.user
            pre_save_address.save()
            messages.success(request, 'Endereço cadastrado com sucesso!')
            return redirect('address')
        else:
            print('formulario invalido')
            return render(request, 'add_address.html')

    return render(request, 'add_address.html', {'form_add_address': forms.AddressForm})


def delete_address(request, pk):
    if request.method == 'GET':
        raise Http404('Página não encontrada!')

    address = models.AddressUser.objects.get(id=pk)
    address.delete()
    messages.success(request, 'O endereço foi excluído com sucesso!')
    return redirect('address')


@login_required(login_url='login')
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
        'address': models.AddressUser.objects.filter(user=request.user, active=True)
    }

    return render(request, 'my_info.html', context)


@login_required(login_url='login')
def edit_profile(request, pk):
    data_profile = DataUser.objects.get(user_profile=request.user, id=pk)

    form = forms.ProfileForm(request.POST or None, instance=data_profile)
    context = {
        'data_profile': data_profile,
        'form': form
    }

    if request.POST:
        if form.is_valid():
            # Salva alteração de dados do usuário
            data_profile.user_profile.first_name = form.cleaned_data.get('first_name')
            data_profile.user_profile.last_name = form.cleaned_data.get('last_name')
            data_profile.user_profile.email = form.cleaned_data.get('email')
            data_profile.user_profile.save()

            # Salva alteração de dados do perfil
            data_profile.cell_phone = form.cleaned_data.get('cell_phone')
            data_profile.save()
            messages.success(request, 'Salvo com sucesso!')

            return redirect('info')
        else:
            messages.info(request, 'Algo deu errado, tente novamente!')
            return render(request, 'edit_profile.html', context)
    else:
        return render(request, 'edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    form = forms.ChangePassword(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Senha alterada com sucesso!')
            return render(request, 'change_password.html', {'form': form})
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        return render(request, 'change_password.html', {'form': form})
