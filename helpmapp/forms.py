#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import *

class HelpMapperForm(forms.Form):
    class Meta:
        model = HelpMapper
        fields = ('nombre', 'apellido', 'nombreUsuario', 'contrasena', 'sexo', 'cedula',
                    'tipoSangre', 'telefono', 'correo', 'habilidad', 'estado')

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput,label='Nombre de usuario', max_length=16)
   
class RecoveryForm(forms.Form):
    correo = forms.CharField(label='Correo Electrónico', max_length=100)
    