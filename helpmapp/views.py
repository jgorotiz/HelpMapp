#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from daw.settings import EMAIL_HOST_USER
from django.contrib import messages
import random, string
import json
from .forms import *

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def mostrar_indice(request):
    return render(request,'helpmapp/cliente/index.html')

def recovery(request):
    if request.method=='GET':
        form = RecoveryForm()
        return render(request, 'helpmapp/cliente/recovery.html', {'form': form})

    elif request.method=='POST':
        #send_mail("Cambio de contrasena", "Post", EMAIL_HOST_USER, ['ramsesfabri@gmail.com]'],fail_silently=False)

        # create a form instance and populate it with data from the request:
        form = RecoveryForm(request.POST)
        print(request.POST)
        developers = ["Fabricio","Galo", "María Belén", "Jonathan"]

        # check whether it's valid:
        if form.is_valid():
            print("is valid")
            # process the data in form.cleaned_data as required      
            # redirect to a new URL:
            data = form.cleaned_data
            text = "Su cambio de contraseña ha sido exitoso. Por favor, ingrese con su nueva contraseña: "
            text += id_generator(8)
            text += "\n "
            text += "Atentamente,\n"
            text += developers[random.randint(0,len(developers)-1)] + ", del Equipo de helpMapp."
            #send_mail("Vales trozo", "Post", EMAIL_HOST_USER, ['ramsesfabri@gmail.com]'],fail_silently=False)

            send_mail("Cambio de contraseña", text, EMAIL_HOST_USER, [data['correo']],fail_silently=False)
            return render(request, 'helpmapp/cliente/login.html')

    return render(request, 'helpmapp/cliente/recovery.html', {'form': form})




def mostrar_tutoriales(request):
    return render(request,'helpmapp/cliente/tutoriales.html')

def mostrar_voluntario(request):
    return render(request,'helpmapp/cliente/voluntario.html')

def listar_voluntario(request):
    voluntarios =  AyudadorMapa.objects.all()
         
    return render(request, 'helpmapp/cliente/prueba.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntaryForm(request.POST)
        if form.is_valid():
            voluntario = form.save(commit=False)
            voluntario.save()
            return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})
        else:
            print ('no es valido')

    else:
        form = VoluntaryForm()

    return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})




def mostrar_sobreNosotros(request):
    return render(request,'helpmapp/cliente/aboutus.html')

def mostrar_login(request):
    return render(request,'helpmapp/cliente/login.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VoluntaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

        	 # redirect to a new URL:
            data = form.cleaned_data
            print (data['nombre'])
            print (data['apellido'])
            print (data['cedula'])
            #print data['GENDER_CHOICES']
            print (data['trabajo_campo'])
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VoluntaryForm()

    return render(request, 'helpmapp/voluntario.html', {'form': form})
def show_name(request):
	
	return render(request,'helpmapp/prueba.html')

#LOGIN DEL ADMINISTRADOR
def mostrar_loginAdmin(request):
    if (not "member_id" in request.session.keys()):
        if request.method == 'POST':
            form= LoginForm(request.POST)
            if form.is_valid():
                try:
                    m = Administrador.objects.get(nombreUsuario=request.POST['username'])
                    print(m.contrasena== request.POST['password'])
                    if m.contrasena == request.POST['password']:
                        request.session['member_id'] = m.nombreUsuario
                        request.session['tipo'] = m.tipo
                        if (m.tipo==0): #es super admin
                            return render(request,'helpmapp/Administrador/superAdmin/index.html')
                        else:#es admin de centro de acopio
                            return HttpResponseRedirect('/administradorZonal/')
                    else:
                        messages.error(request, "Credenciales incorrectas")
                except: 
                    messages.error(request,"Usuario no registrado")
        else:
            form= LoginForm()
        return render(request,'helpmapp/Administrador/index.html',{'form': form})
    else:
        if (request.session['tipo']==0): #es super admin
            return render(request,'helpmapp/Administrador/superAdmin/index.html')
        else:#es admin de centro de acopio            
            return HttpResponseRedirect('/administradorZonal/')


#CERRAR SESIÓN DE ADMIN
def cerrarSesion(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    
    return HttpResponseRedirect('/loginAdmin/')
    

#MOSTRAR INDEX DEL SUPER ADMIN
#@login_required(login_url='/loginAdmin/')
#@permission_required('helpmapp.is_superadmin', login_url='/loginAdmin/')
# def mostrar_administradorGeneral(request):
#     if('member_id' in request.session):
#         return render(request,'helpmapp/Administrador/superAdmin/index.html')
#     else:
#         return redirect('helpmapp/Administrador/index.html')
def mostrar_administradorGeneral(request):
    if('member_id' in list(request.session.keys())):
        return render(request,'helpmapp/Administrador/superAdmin/index.html')
    return HttpResponseRedirect('/loginAdmin/')

def mostrar_administradorZonal(request):
    if('member_id' in list(request.session.keys())):
        return render(request,'helpmapp/Administrador/adminCentro/index.html')
#     if('member_id' in list(request.session.keys())):

    return HttpResponseRedirect('/loginAdmin/')

def mostrar_configuracionCapacidades(request):
    if('member_id' in request.session):
        m = Administrador.objects.get(nombreUsuario=request.session["member_id"])
        if (m.tipo==1): #si es administrador de centro
            if(request.method=="POST"):
                form = CapacidadesForm(request.POST)
                if form.is_valid():
                    centro=CentroAcopio.objects.get(id=m.idCentro)
                    data = form.cleaned_data
                    cagua=data["maxagua"]
                    cropa=data["maxropa"]
                    ccomida=data["maxcom"]
                    centro.capacidad_agua=cagua
                    centro.capacidad_ropa=cropa
                    centro.capacidad_comida=ccomida
                    centro.save()
            
                    return render(request, 'helpmapp/Administrador/adminCentro/configuracionCapacidades.html', {'form': form})
                else:
                    print ('no es valido')

            else:
                print ('no es post')
                form = CapacidadesForm()
                return render(request,'helpmapp/Administrador/adminCentro/configuracionCapacidades.html', {'form': form})
        return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')
    #return render(request,'helpmapp/Administrador/adminCentro/configuracionCapacidades.html')

def mostrar_configuracionCuenta(request):
    return render(request,'helpmapp/Administrador/adminCentro/configuracionCuenta.html')

def mostrar_crearProducto(request):
    return render(request,'helpmapp/Administrador/superAdmin/crearProducto.html')

def mostrar_inventarioAgua(request):
    return render(request,'helpmapp/Administrador/adminCentro/inventarioAgua.html')

def mostrar_inventarioComida(request):
    if(request.session["member_id"]):
        if(request.session["tipo"]==1):
            comida=Producto.objects.filter(idCategoria=1) #id de comida
            kg=0
            for c in comida:
                kg+=c.cantidad
            ropas=Producto.objects.filter(idCategoria=2) # id de ropa
            ropa=0
            for r in ropas:
                ropa+=r.cantidad
            agua=Producto.objects.filter(idCategoria=3) #id de agua
            l=0
            for a in agua:
                l+=a.cantidad
            lista2=[]
            lista2.append(float(kg))
            lista2.append(float(ropa))
            lista2.append(float(l))
            print (lista2)
            #lista=json.dumps(lista2)
            lista=lista2
            return render(request,'helpmapp/Administrador/adminCentro/inventarioComida.html',{'lista':lista})

    return HttpResponseRedirect('/loginAdmin/')

def mostrar_inventarioRopa(request):
    return render(request,'helpmapp/Administrador/adminCentro/inventarioRopa.html')

def mostrar_buscarCentroAcopio(request):
    return render(request,'helpmapp/Administrador/superAdmin/buscarCentroAcopio.html')

def mostrar_configCuenta(request):
    return render(request,'helpmapp/Administrador/superAdmin/configCuenta.html')

#CREAR UNA CUENTA DE ADMINISTRADOR    
def mostrar_crearAdministrador(request):
    if request.method == 'POST':
        
        form = AdministradorForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.save()

    else:    
        form = AdministradorForm()
   
    return render(request,'helpmapp/Administrador/superAdmin/crearAdmin.html',{'form': form})

def mostrar_verCentro(request):
    return render(request,'helpmapp/Administrador/superAdmin/verCentro.html')

def mostrar_recuperarCuenta(request):
    return render(request,'helpmapp/Administrador/superAdmin/recuperarCuenta.html')


def saveData():
    return


#devolver todos los centros de acopios
def listar_centroAcopio(request):
    centros =  CentroDeAcopio.objects.all()
    return render(request, 'helpmapp/cliente/donar.html', {'centros': centros})



#Registrar helpmapper
def registrar_helpmapper(request):
    if request.method == 'POST':
        print ('si es post')
        form = HelpMapper(request.POST)
        if form.is_valid():
            print ('si es valid')
            helpmapper = form.save(commit=False)
            helpmapper.save()
            return render(request, 'helpmapp/cliente/index.html', {'form': form})
        else:
            print ('no es valido')
    else:
        print ('no es post')
        form = HelpMapperForm()
    return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})

def actualizar_contrasena(request, nombreUsuario):
    helpmapper = get_object_or_404(HelpMapper, pk=nombreUsuario)
    if request.method == "POST":
        form = HelpMapperForm(request.POST,instance=helpmapper)
        if form.is_valid():
            helpmapper = form.save(commit=False)
            helpmapper.save()
            return redirect('helpmapp/cliente/index.html')
    else:
            form = HelpMapperForm(instance=helpmapper)
    return render(request, 'helpmapp/cliente/index.html', {'form': form})

def eliminar_helpmapper(request, nombreUsuario):
    
    helpmapper  = get_object_or_404(HelpMapper, pk = nombreUsuario).delete()

    return HttpResponseRedirect('/')

def obtener_datos(request):
    print("Es administrador zonal")
    comida=Producto.objects.filter(idCategoria=1) #id de comida
    kg=0
    for c in comida:
        kg+=c.cantidad
    ropa=Producto.objects.filter(idCategoria=2).count() # id de ropa
   
    agua=Producto.objects.filter(idCategoria=3) #id de agua
    l=0
    for a in agua:
        l+=a.cantidad
    lista=[kg,ropa,l]
    return lista





#estadistica Grafico pra cliente

def mostrar_GraficoEstaditico(request):
    comida=Producto.objects.filter(idCategoria=1) #id de comida
    kg=0
    for c in comida:
        kg+=c.cantidad
    ropas=Producto.objects.filter(idCategoria=2) # id de ropa
    ropa=0
    for r in ropas:
        ropa+=r.cantidad
    agua=Producto.objects.filter(idCategoria=3) #id de agua
    l=0
    for a in agua:
        l+=a.cantidad
    lista2=[]
    lista2.append(float(kg))
    lista2.append(float(ropa))
    lista2.append(float(l))
    print (lista2)
    #lista=json.dumps(lista2)
    lista=lista2
    return render(request,'helpmapp/cliente/statistics.html',{'lista':lista})

