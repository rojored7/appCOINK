from tkinter import Widget
from django import forms

from .models import User


class FormularioUsuarios(forms.ModelForm):
    class Meta:
        model = User
        fields=('name_user','emai','ciudad')

        