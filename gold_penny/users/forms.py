from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=30)
    password = forms.CharField(
        label='Senha',
        max_length=50,
        widget=forms.PasswordInput
    )
