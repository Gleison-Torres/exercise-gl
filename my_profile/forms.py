from django import forms
from .models import AddressUser
from django.contrib.auth.models import User


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressUser
        fields = (
            'sender_name', 'postal_code', 'street_address',
            'number_address', 'neighborhood', 'additional_info', 'city', 'state', 'type_address', 'active'
        )

        widgets = {
            'type_address': forms.RadioSelect,
            'city': forms.TextInput(attrs={'readonly': True}),
            'state': forms.TextInput(attrs={'readonly': True}),
        }


class ProfileForm(forms.ModelForm):
    cell_phone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(attrs={'placeholder': '(99) 12345-6789'})
    )

    cpf = forms.CharField(
        label='CPF',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-00', 'readonly': True})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'cpf')

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'})


        }


class PasswordChange(forms.Form):
    old_password = forms.CharField(
        label='Senha atual', widget=forms.PasswordInput(attrs={'placeholder': 'Senha atual'})
    )

    new_password = forms.CharField(
        label='Nova senha', widget=forms.PasswordInput(attrs={'placeholder': 'Nova senha'})
    )

    confirm_new_password = forms.CharField(
        label='Confirme a nova senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a nova senha'})
    )

