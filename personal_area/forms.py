from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'Логин',
                'value': ''
            }
        ),
        label=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'Пароль',
                'value': ''
            }
        ),
        label=False
    )
