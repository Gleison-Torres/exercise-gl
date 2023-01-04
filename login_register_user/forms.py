from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        required=True,
        help_text='Obrigatório pelo menos uma letra maiúscula'
    )

    confirm_password = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha'}),
        required=True,
        help_text='Senha e Confirmação de senha devem ser iguais.'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'E-mail'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'})
        }


class LoginForm(forms.Form):
    user_customer = forms.CharField(
        label='Usuário',
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))

    password_customer = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

