from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
    )

    confirm_password = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

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

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password_1 = cleaned_data.get('password')
        password_2 = cleaned_data.get('confirm_password')

        if password_1 != password_2:
            raise ValidationError(
                {'password': 'As senhas devem ser iguais!',
                 'confirm_password': 'As senhas devem ser iguais!'}
            )

        if password_1 == password_2:
            if len(password_1) < 8:
                raise ValidationError({
                    'password': 'A senha deve conter no mínimo 8 caracteres e uma letra maiúscula',
                    'confirm_password': 'A senha deve conter no mínimo 8 caracteres e uma letra maiúscula'})

            elif len(password_1) >= 8:
                upper_char = 0  # Contador de letras maiúsculas na senha.
                special_char = 0  # Contador de caracteres especiais.

                for digit in password_1:  # Verifica se "password_1" tem letras maiúsculas e caracteres especiais.
                    if digit.isupper():
                        upper_char += 1
                    if digit in '#@$%¨&*()<>?.,/':  # Verifica se existe caracteres especiais na senha.
                        special_char += 1

                if upper_char == 0:
                    raise ValidationError(
                        {'password': 'A senha deve conter pelo menos uma letra maiúscula!',
                         'confirm_password': 'A senha deve conter pelo menos uma letra maiúscula!'})

                if special_char == 0:
                    raise ValidationError(
                        {'password': 'A senha deve conter caracteres especiais',
                         'confirm_password': 'A senha deve conter caracteres especiais'})

    def clean_username(self):
        name_user = self.cleaned_data.get('username')
        exist = User.objects.filter(username=name_user).exists()
        if exist:
            raise ValidationError('Usuário já existe!')
        return name_user


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))


