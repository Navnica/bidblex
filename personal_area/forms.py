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


class ProfileDetailsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        self.fields['username'].initial = self.request.user.username
        self.fields['email'].initial = self.request.user.email

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field',
                'readonly': True
            }
        ),
        label='Никнейм'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'text-field',
                'readonly': True
            }
        ),
        label='E-Mail'
    )


class ContactDataForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field',
            }
        ),
        label='ФИО'
    )

    phone = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={

            }
        ),
        label='Номер телефона'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'text-field',
            }
        ),
        label='E-Mail'
    )
