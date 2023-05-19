from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import News, User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'media', 'category']


class UpdateUserInfoForm(forms.ModelForm):
    first_name = forms.CharField(max_length=65),
    last_name = forms.CharField(max_length=65),
    username = forms.CharField(max_length=65),

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UpdateUserImageForm(forms.ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['avatar']
