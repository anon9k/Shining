from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Apelido')
    email = forms.EmailField()
    is_staff = forms.BooleanField()
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_staff':
                self.fields[field].widget.attrs.update({'class':'form-control'})


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

