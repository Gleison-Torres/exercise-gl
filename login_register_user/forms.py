from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
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

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        required=True,
    )

    confirm_password = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha'}),
        required=True,
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password_1 = cleaned_data.get('password')
        password_2 = cleaned_data.get('confirm_password')

        if password_1 != password_2:
            raise ValidationError(
                {'password': 'As senhas devem ser iguais!',
                 'confirm_password': 'As senhas devem ser iguais!'}
            )

    def clean_username(self):
        name_user = self.cleaned_data.get('username')
        exist = User.objects.filter(username=name_user).exists()
        if exist:
            raise ValidationError('Usuário já existe!')
        return name_user


class LoginForm(forms.Form):
    user_customer = forms.CharField(
        label='Usuário',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))

    password_customer = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))


