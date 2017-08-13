from django import forms
from .models import *

class VoluntaryForm(forms.Form):
    nombre = forms.CharField(label='Nombres')
    apellido=forms.CharField(label='Apellidos')
    cedula=forms.CharField(label='Cedula')
    tipo_sangre=forms.ChoiceField(label="Tipo de sangre")
    GENDER_CHOICES = (('M', 'Masculino'),('F', 'Femenino'))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    telefono=forms.CharField(label='Telefono')
    email=forms.EmailField(label="Correo")
    suscribe = forms.BooleanField(required=False)
    auxilios=forms.BooleanField(required=False)
    culinarias=forms.BooleanField(required=False)
    trabajo_campo=forms.BooleanField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput,label='Nombre de usuario', max_length=16)
   
class RecoverForm(forms.Form):
    correo = forms.CharField(label='Correo Electrónico', max_length=100)