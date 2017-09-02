#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from daw.settings import EMAIL_HOST_USER
from django.contrib import messages
import random, string
import json
from .forms import *
from django.db import connection

#Controllers for everyone
def mostrar_indice(request):
    return render(request,'helpmapp/cliente/not_logged/index.html')

#devolver todos los centros de acopios
def listar_centroAcopio(request):
    centros =  CentroDeAcopio.objects.all()
    return render(request, 'helpmapp/cliente/not_logged/donar.html', {'centros': centros})

def mostrar_voluntario(request):
    return render(request,'helpmapp/cliente/not_logged/voluntario.html')

def mostrar_sobreNosotros(request):
    return render(request,'helpmapp/cliente/not_logged/aboutus.html')

def mostrar_login(request):
    return render(request,'helpmapp/cliente/not_logged/login.html')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def recovery(request):
    if request.method=='GET':
        form = RecoveryForm()
        return render(request, 'helpmapp/cliente/not_logged/recovery.html', {'form': form})

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

            try:
                hm = HelpMapper.objects.get(correo=data['correo'])
                if data['correo'] == hm.correo:
                    print("ENVIANDO...")
                    remiter= developers[random.randint(0,len(developers)-1)] + " del Equipo de helpMapp, te saluda e informa que: \n"
                    text = remiter + "Tu cambio de contraseña ha sido exitoso. Por favor, ingresa con tu nueva contraseña: "
                    new_contrasena = id_generator(8)
                    text += new_contrasena+ "\n" + "Gracias por ser un helpMapper!"
         
                    hm.contrasena = new_contrasena
                    hm.save()
                    #send_mail("Vales trozo", text, EMAIL_HOST_USER, ['rodfcast@gmail.com]'],fail_silently=False)
                    send_mail("helpMapp: Cambio de contraseña", text, EMAIL_HOST_USER, [data['correo']],fail_silently=False)
                    return render(request, 'helpmapp/cliente/not_logged/message.html', {'title': 'Correo Enviado', 'message':'Su nueva contraseña ha sido enviada al correo registrado.'} )
            except Exception as e:
                return render(request, 'helpmapp/cliente/not_logged/message.html', {'title': 'Correo Inválido', 'message':'El correo ingresado es incorrecto.'})
                pass
    return render(request, 'helpmapp/cliente/not_logged/message.html', {'form':form})


#For HelpMappers

def index_hm(request):
    return render(request,'helpmapp/cliente/helpmapper/index.html')

#devolver todos los centros de acopios
def listar_centroAcopioHM(request):

    centros =  CentroDeAcopio.objects.all()

    return render(request, 'helpmapp/cliente/helpmapper/donar.html', {'centros': centros})

#estadistica Grafico pra cliente
def mostrar_GraficoEstadistico(request):
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
    return render(request,'helpmapp/cliente/helpmapper/statistics.html',{'lista':lista})

def mostrar_tutoriales(request):
    return render(request,'helpmapp/cliente/helpmapper/tutoriales.html')

def mostrar_sobreNosotrosHM(request):

    return render(request,'helpmapp/cliente/helpmapper/aboutus.html')






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
                            return HttpResponseRedirect('/administradorGeneral/')
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
            upc = CentroDeAcopio.objects.get(idAdmin=request.session['member_id'])
            return render(request,'helpmapp/Administrador/adminCentro/index.html',{'upc':upc})


#CERRAR SESIÓN DE ADMIN
def cerrarSesion(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    
    return HttpResponseRedirect('/loginAdmin/')


#PÁGINAS DEL ADMINISTRADOR GENERAL
def mostrar_administradorGeneral(request):
    if('member_id' in list(request.session.keys())):
        print("hola")
        return render(request,'helpmapp/Administrador/superAdmin/index.html')
    else:
        return HttpResponseRedirect('/loginAdmin/')

def buscarCentroAcopio(request):
    return render(request,'helpmapp/Administrador/superAdmin/buscarCentroAcopio.html')

def mostrar_configCuenta(request):
    return render(request,'helpmapp/Administrador/superAdmin/configCuenta.html')
#CREAR UNA CUENTA DE ADMINISTRADOR    
def mostrar_crearAdministrador(request):
    # if request.method == 'POST':
        
    #     form = AdministradorForm(request.POST)
    #     if form.is_valid():

    #         user = form.save(commit=False)
    #         user.save()

    # else:    
    #     form = AdministradorForm()
   
    return render(request,'helpmapp/Administrador/superAdmin/crearAdmin.html')
def mostrar_verCentro(request):
    return render(request,'helpmapp/Administrador/superAdmin/verCentro.html')

def mostrar_crearProducto(request):
    print("hola2")
    if(request.session.get('member_id',None) != None):
        return render(request,'helpmapp/Administrador/superAdmin/crearProducto.html')
    else:
        return HttpResponseRedirect('/loginAdmin/')


#PÁGINAS DEL ADMINISTRADOR ZONAL
def mostrar_administradorZonal(request):
    if('member_id' in list(request.session.keys())):
        print(request.session["member_id"])
        upc = CentroDeAcopio.objects.get(idAdmin=request.session['member_id'])
        return render(request,'helpmapp/Administrador/adminCentro/index.html',{'upc':upc})
#     if('member_id' in list(request.session.keys())):

    return HttpResponseRedirect('/loginAdmin/')

def mostrar_configuracionCapacidades(request):
    # if('member_id' in request.session.keys()):
    #     m = Administrador.objects.get(nombreUsuario=request.session["member_id"])
    #     if (m.tipo==1): #si es administrador de centro
    #         if(request.method=="POST"):
    #             form = CapacidadesForm(request.POST)
    #             if form.is_valid():
    #                 centro=CentroAcopio.objects.get(id=m.idCentro)
    #                 data = form.cleaned_data
    #                 cagua=data["maxagua"]
    #                 cropa=data["maxropa"]
    #                 ccomida=data["maxcom"]
    #                 centro.capacidad_agua=cagua
    #                 centro.capacidad_ropa=cropa
    #                 centro.capacidad_comida=ccomida
    #                 centro.save()
            
    #                 return render(request, 'helpmapp/Administrador/adminCentro/configuracionCapacidades.html', {'form': form})
    #             else:
    #                 print ('no es valido')

    #         else:
    #             print ('no es post')
    #             form = CapacidadesForm()
    #             return render(request,'helpmapp/Administrador/adminCentro/configuracionCapacidades.html', {'form': form})
    #     return HttpResponseRedirect('/administradorGeneral/')
    # return HttpResponseRedirect('/loginAdmin/')
    return render(request,"helpmapp/Administrador/adminCentro/configuracionCapacidades.html")

def mostrar_configuracionCuenta(request):
    return render(request,'helpmapp/Administrador/adminCentro/configuracionCuenta.html')


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



def profile(request):
    return render(request,'helpmapp/cliente/helpmapper/profile.html')

def logout(request):
    return redirect(request,'helpmapp/cliente/not_logged/index.html')





def mostrar_recuperarCuenta(request):
    return render(request,'helpmapp/Administrador/superAdmin/recuperarCuenta.html')


def saveData():
    return






#Registrar helpmapper
def registrar_helpmapper(request):
    if request.method == 'POST':
        print ('si es post')
        form = HelpMapperForm(request.POST)
        if form.is_valid():
            print ('si es valid')
            helpmapper = form.save(commit=False)
            helpmapper.save()
            return render(request, 'helpmapp/cliente/donar.html', {'form': form})
        else:
            print ('no es valido')
    else:
        print ('no es post')
        form = HelpMapperForm()
    return render(request, 'helpmapp/cliente/donar.html', {'form': form})

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
   
    response_data={}
    l=[] #diccionario que contendrá la cantidad de cada prenda de ropa
    ropa=Producto.objects.filter(idCategoria=2) #filtro todos los productos que sean ropa
    maxropa=0
    for r in ropa:
        prendas=ExistenciaInventario.objects.filter(idProducto=r.id) #filtro todos los inventariados por cada prenda
        c=prendas.cantidad.sum()
        if(c>maxropa):
            maxropa=c
        d={}
        d["dept"]=r.nombre
        d["age"]=c
        l.append(d)
    response_data["cantidad_ropa"]=l
    response_data["max_ropa"]=maxropa

    
    comida=Producto.objects.filter(idCategoria=1)
    hoy=datetime.date.today()
    fecha=hoy-datetime.timedelta(days=7)
    cursor=connection.cursor()
    resultados=cursor.execute("SELECT fecha, SUM(IF(accion=\'enviar\',cantidad,0)) as \'enviar\' FROM CambioInventario,Producto WHERE CambioInventario.idProducto=Producto.idProducto and idCategoria=1 and fecha>="+fecha)
    resultados=dictfetchall(cursor) #de la forma [{'fecha': jfahsdf,'enviar':239},{'fecha': jferwsdf,'enviar':230}]
    response_data["comida_enviada"]=resultados
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    
   






