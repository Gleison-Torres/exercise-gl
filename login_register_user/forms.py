from django import forms


class LoginForm(forms.Form):
    user_customer = forms.CharField(
        label='Usuário',
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))

    password_customer = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

