from django import forms
from .models import AddressUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.core.exceptions import ValidationError


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


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        label='Senha antiga',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha antiga', 'autofocus': True})
    )

    new_password1 = forms.CharField(
        label='Nova senha',
        help_text='A senha deve conter pelo menos 8 caracteres, '
                  'incluir letras maiúsculas, minúsculas, números e caracteres especiais. ',
        widget=forms.PasswordInput(attrs={'placeholder': 'Nova senha'})
    )

    new_password2 = forms.CharField(
        label='Repita a nova senha', widget=forms.PasswordInput(attrs={'placeholder': 'Repita a nova senha'})
    )

    def clean(self):
        cleaned_data = super(ChangePassword, self).clean()
        pass1 = cleaned_data.get('new_password1')
        pass2 = cleaned_data.get('new_password2')

        if pass1 == pass2:
            if len(pass1) >= 8:
                upper_char = 0  # Contador de letras maiúsculas na senha.
                special_char = 0  # Contador de caracteres especiais.

                for digit in pass1:  # Verifica se "password_1" tem letras maiúsculas e caracteres especiais.
                    if digit.isupper():
                        upper_char += 1
                    if digit in '#@$%¨&*()<>?.,/':  # Verifica se existe caracteres especiais na senha.
                        special_char += 1

                if upper_char == 0:
                    raise ValidationError(
                        {'new_password1': 'Use letras maiúsculas e minúsculas!',
                         'new_password2': 'Use letras maiúsculas e minúsculas! '})

                if special_char == 0:
                    raise ValidationError(
                        {'new_password1': 'Use caracteres especiais!',
                         'new_password2': 'Use caracteres especiais!'})

                if self.user.check_password(pass2):  # Verifica se a senha contem números.
                    raise ValidationError(
                        {'new_password1': 'A nova senha não pode ser igual a senha antiga.',
                         'new_password2': 'A nova senha não pode ser igual a senha antiga.'}
                    )
