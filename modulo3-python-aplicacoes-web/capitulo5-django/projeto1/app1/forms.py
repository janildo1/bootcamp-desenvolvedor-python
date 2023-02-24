from django import forms
from .models import user

# modelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['nome', 'telefone', 'email']

# form.Form
