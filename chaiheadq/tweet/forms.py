from django import forms
from .models import Tweet
from django.contrib.auth.froms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "photo"]


class UserRegistrationForm(UserCreationForm):
    email = froms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]