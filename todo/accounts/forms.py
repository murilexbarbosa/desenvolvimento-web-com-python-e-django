from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    attrs = {
        "type": "password"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
