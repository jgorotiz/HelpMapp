#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import *

class HelpMapperForm(forms.ModelForm):
    class Meta:
        model = HelpMapper
        fields = ('nombre', 'apellido', 'nombre_usuario', 'contrasena', 'sexo', 'cedula',
                    'tipo_sangre', 'telefono', 'correo', 'habilidad', 'estado')

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput,label='Nombre de usuario', max_length=16)
   
class RecoveryForm(forms.Form):
    correo = forms.CharField(label='Correo Electrónico', max_length=100,required=True)
    
class ChangePassForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput,label='Contrasena', max_length=16)
	confirm_password = forms.CharField(widget=forms.PasswordInput,label='Confirmar contrasena', max_length=16)

class HelpMapperForm(forms.ModelForm):
    class Meta:
        model = HelpMapper
        fields = ('nombre', 'apellido', 'nombre_usuario', 'contrasena', 'sexo', 'cedula',
                    'tipo_sangre', 'telefono', 'correo', 'habilidad', 'estado')
