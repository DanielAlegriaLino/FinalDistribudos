from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Historial
from datetime import date

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmailForm(forms.Form):
    email = forms.EmailField()

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['code']

    def save(self, commit=True):
        self.instance.date = date.today()
        self.instance.user = self.user
        return super().save(commit)

