from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'Имя пользователя',
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


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'Имя пользователя',
                'value': ''
            }
        ),
        label=False
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'E-Mail',
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

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-field',
                'placeholder': 'Подтверждение',
                'value': ''
            }
        ),
        label=False
    )
