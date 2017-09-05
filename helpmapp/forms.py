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
    


class configurarCapacidadesForm(forms.Form):
	almacenamiento_agua = forms.DecimalField(label='Capacidad máxima de agua:',max_digits=8)
	almacenamiento_ropa = forms.DecimalField(label='Capacidad máxima de ropa:',max_digits=8)
	almacenamiento_comida = forms.DecimalField(label='Capacidad máxima de Comida:',max_digits=8)

class ChangePassForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput,label='Contrasena', max_length=16)
	confirm_password = forms.CharField(widget=forms.PasswordInput,label='Confirmar contrasena', max_length=16)


class ChangePassAdminForm(forms.Form):
    password_actual = forms.CharField(widget=forms.PasswordInput,label='Contrasena Actual', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput,label='Contrasena', max_length=16)
    confirm_password = forms.CharField(widget=forms.PasswordInput,label='Confirmar contrasena', max_length=16)



class AdminForm(forms.ModelForm):
    class Meta:
        model = Administrador
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
        fields = ( 'nombre_usuario', 'contrasena', 'correo')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ( 'nombre_producto', 'id_categoria')


class agregarComida(forms.Form):
    id_producto = forms.CharField( label='id producto')
    id_centro = forms.CharField( label='id centro')
    cantidad = forms.DecimalField(label='Cantidad',max_digits=6)

