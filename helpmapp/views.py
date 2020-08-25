#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import string

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from daw.settings import EMAIL_HOST_USER
from .forms import *
from .models import *


# Decorator for authentication.
def authenticated(func):
    """
    Receives a django view function and decorates it with an session cookie check
    :param func:
    :return:
    """

    def _wrapped_func(*args, **kwargs):
        request = args[0]
        if 'member_id' in request.session:
            return func(*args, **kwargs)
        else:
            return redirect('/')

    return _wrapped_func


# Controllers for everyone
def mostrar_indice(request):
    return render(request, 'helpmapp/cliente/not_logged/index.html')


# devolver todos los centros de acopios
def listar_centroAcopio(request):
    centros = CentroDeAcopio.objects.all()
    if request.method == 'POST':
        form = coordenadasForm(request.POST)
        data = form.cleaned_data
        if form.is_valid():
            latitud = data['latitud']
            longitud = data['longitud']
            return render(request, 'helpmapp/cliente/not_logged/donar.html',
                          {'centros': centros, 'latitud': latitud, 'longitud': longitud})
    return render(request, 'helpmapp/cliente/not_logged/donar.html', {'centros': centros})


def mostrar_sobreNosotros(request):
    return render(request, 'helpmapp/cliente/not_logged/aboutus.html')


def mostrar_login(request):
    if "member_id" not in request.session.keys():
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                try:
                    m = HelpMapper.objects.get(nombre_usuario=request.POST['username'])
                    print(m.contrasena == request.POST['password'])
                    if m.contrasena == request.POST['password']:
                        request.session['member_id'] = m.nombre_usuario
                        print(request.session['member_id'])
                        return HttpResponseRedirect('/home/')
                    else:
                        messages.error(request, "Credenciales incorrectas")
                except:
                    messages.error(request, "Usuario no registrado")
            else:
                form = LoginForm()
        else:
            form = LoginForm()
            print(form)
        return render(request, 'helpmapp/cliente/not_logged/login.html', {'form': form})
    else:
        print(request.session['member_id'])
        usuario = HelpMapper.objects.get(nombre_usuario=request.session['member_id'])
        return render(request, 'helpmapp/cliente/helpmapper/index.html', {'usuario': usuario})


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@authenticated
def recovery(request):
    if request.method == 'GET':
        form = RecoveryForm()
        return render(request, 'helpmapp/cliente/not_logged/recovery.html', {'form': form})

    elif request.method == 'POST':
        # send_mail("Cambio de contrasena", "Post", EMAIL_HOST_USER, ['ramsesfabri@gmail.com]'],fail_silently=False)

        # create a form instance and populate it with data from the request:
        form = RecoveryForm(request.POST)
        print(request.POST)
        developers = ["Fabricio", "Galo", "María Belén", "Jonathan"]

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
                    remiter = developers[random.randint(0, len(
                        developers) - 1)] + " del Equipo de helpMapp, te saluda e informa que: \n"
                    text = remiter + "Tu cambio de contraseña ha sido exitoso. Por favor, ingresa con tu nueva contraseña: "
                    new_contrasena = id_generator(8)
                    text += new_contrasena + "\n" + "Gracias por ser un helpMapper!"

                    hm.contrasena = new_contrasena
                    hm.save()
                    # send_mail("Vales trozo", text, EMAIL_HOST_USER, ['rodfcast@gmail.com]'],fail_silently=False)
                    send_mail("helpMapp: Cambio de contraseña", text, EMAIL_HOST_USER, [data['correo']],
                              fail_silently=False)
                    return render(request, 'helpmapp/cliente/not_logged/message.html', {'title': 'Correo Enviado',
                                                                                        'message': 'Su nueva contraseña ha sido enviada al correo registrado.'})
            except Exception as e:
                return render(request, 'helpmapp/cliente/not_logged/message.html',
                              {'title': 'Correo Inválido', 'message': 'El correo ingresado es incorrecto.'})
                pass
    return render(request, 'helpmapp/cliente/not_logged/message.html', {'form': form})

@authenticated
def index_hm(request):
    return render(request, 'helpmapp/cliente/helpmapper/index.html')


# devolver todos los centros de acopios
@authenticated
def listar_centroAcopioHM(request):
    centros = CentroDeAcopio.objects.all()

    return render(request, 'helpmapp/cliente/helpmapper/donar.html', {'centros': centros})


# estadistica Grafico pra cliente
def mostrar_GraficoEstadistico(request):
    # comida=Producto.objects.filter(id_categoria=1) #id de comida
    # kg=0
    # for c in comida:
    #     kg+=c.cantidad
    # ropas=Producto.objects.filter(id_categoria=2) # id de ropa
    # ropa=0
    # for r in ropas:
    #     ropa+=r.cantidad
    # agua=Producto.objects.filter(id_categoria=3) #id de agua
    # l=0
    # for a in agua:
    #     l+=a.cantidad
    # lista2=[]
    # lista2.append(float(kg))
    # lista2.append(float(ropa))
    # lista2.append(float(l))
    # print (lista2)
    # #lista=json.dumps(lista2)
    # lista=lista2
    return render(request, 'helpmapp/cliente/helpmapper/statistics.html')


def mostrar_tutoriales(request):
    return render(request, 'helpmapp/cliente/helpmapper/tutoriales.html')

@authenticated
def mostrar_sobreNosotrosHM(request):
    return render(request, 'helpmapp/cliente/helpmapper/aboutus.html')

### TODO: Arreglar este endpoint.
def listar_voluntario(request):
    voluntarios = AyudadorMapa.objects.all()

    return render(request, 'helpmapp/cliente/prueba.html', {'voluntarios': voluntarios})


def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntaryForm(request.POST)
        if form.is_valid():
            voluntario = form.save(commit=False)
            voluntario.save()
            return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})
        else:
            print('no es valido')

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
            print(data['nombre'])
            print(data['apellido'])
            print(data['cedula'])
            # print data['GENDER_CHOICES']
            print(data['trabajo_campo'])
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VoluntaryForm()

    return render(request, 'helpmapp/voluntario.html', {'form': form})


def show_name(request):
    return render(request, 'helpmapp/prueba.html')


# LOGIN DEL ADMINISTRADOR
def mostrar_loginAdmin(request):
    if (not "member_id" in request.session.keys()):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                try:
                    m = Administrador.objects.get(nombre_usuario=request.POST['username'])
                    print(m.contrasena == request.POST['password'])
                    if m.contrasena == request.POST['password']:
                        request.session['member_id'] = m.nombre_usuario
                        request.session['tipo'] = m.tipo
                        if (m.tipo == 0):  # es super admin
                            centros = CentroDeAcopio.objects.all()
                            comida = Producto.objects.filter(id_categoria=1)  # id de comida
                            kg = 0
                            for c in comida:
                                productos = ExistenciaInventario.objects.filter(id_producto=c.id)
                                for p in productos:
                                    kg += p.cantidad

                            ropas = Producto.objects.filter(id_categoria=2)  # id de ropa
                            ropa = 0
                            for r in ropas:
                                productos = ExistenciaInventario.objects.filter(id_producto=r.id)
                                for p in productos:
                                    ropa += p.cantidad
                            aguas = Producto.objects.filter(id_categoria=3)  # id de agua
                            agua = 0
                            for a in aguas:
                                productos = ExistenciaInventario.objects.filter(id_producto=a.id)
                                for p in productos:
                                    agua += p.cantidad
                            centros = CentroDeAcopio.objects.all()
                            return render(request, 'helpmapp/Administrador/superAdmin/index.html',
                                          {'centros': centros, "ropa": ropa, "comida": kg, "agua": agua})

                        else:  # es admin de centro de acopio
                            return HttpResponseRedirect('/administradorZonal/')
                    else:
                        messages.error(request, "Credenciales incorrectas")
                except:
                    messages.error(request, "Usuario no registrado")
        else:
            form = LoginForm()
        return render(request, 'helpmapp/Administrador/index.html', {'form': form})
    else:
        if (request.session['tipo'] == 0):  # es super admin
            centros = CentroDeAcopio.objects.all()
            return render(request, 'helpmapp/Administrador/superAdmin/index.html', {'centros': centros})
        else:  # es admin de centro de acopio
            upc = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
            return render(request, 'helpmapp/Administrador/adminCentro/index.html', {'upc': upc})


# CERRAR SESIÓN DE ADMIN
def cerrarSesion(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass

    return HttpResponseRedirect('/loginAdmin/')


# PÁGINAS DEL ADMINISTRADOR GENERAL
def mostrar_administradorGeneral(request):
    if ('member_id' in list(request.session.keys())):
        comida = Producto.objects.filter(id_categoria=1)  # id de comida
        kg = 0
        for c in comida:
            productos = ExistenciaInventario.objects.filter(id_producto=c.id)
            for p in productos:
                kg += p.cantidad

        ropas = Producto.objects.filter(id_categoria=2)  # id de ropa
        ropa = 0
        for r in ropas:
            productos = ExistenciaInventario.objects.filter(id_producto=r.id)
            for p in productos:
                ropa += p.cantidad
        aguas = Producto.objects.filter(id_categoria=3)  # id de agua
        agua = 0
        for a in aguas:
            productos = ExistenciaInventario.objects.filter(id_producto=a.id)
            for p in productos:
                agua += p.cantidad
        centros = CentroDeAcopio.objects.all()
        return render(request, 'helpmapp/Administrador/superAdmin/index.html',
                      {'centros': centros, "ropa": ropa, "comida": kg, "agua": agua})
    else:
        return HttpResponseRedirect('/loginAdmin/')


def buscarCentroAcopio(request):
    if request.method == 'POST':
        form = filtroForm(request.POST)
        print(form)
        if form.is_valid():
            print("is valid")
            data = form.cleaned_data
            ciudad = data['ciudad'].capitalize()
            upc = CentroDeAcopio.objects.filter(canton=ciudad)
            print(upc)
            return render(request, 'helpmapp/Administrador/superAdmin/buscarCentroAcopio.html', {'upc': upc})
        else:
            print("Not valid")

    return render(request, 'helpmapp/Administrador/superAdmin/buscarCentroAcopio.html')


def mostrar_configCuenta(request):
    if request.method == 'GET':
        form = ChangePassAdminForm()
        return render(request, 'helpmapp/Administrador/superAdmin/configCuenta.html', {'form': form})

    elif request.method == 'POST':
        form = ChangePassAdminForm(request.POST)
        if form.is_valid():
            print("is valid")
            data = form.cleaned_data
            admin = Administrador.objects.get(nombre_usuario=request.session['member_id'])
            if data['password_actual'] == admin.contrasena:
                if data['password'] == data['confirm_password']:
                    admin.contrasena = data['password']
                    admin.save()
                    form = ChangePassAdminForm()
                    return render(request, 'helpmapp/Administrador/superAdmin/configCuenta.html',
                                  {'form': form, 'mensaje': 'Su contraseña ha sido cambiada.'})
                else:
                    form = ChangePassAdminForm()
                    return render(request, 'helpmapp/Administrador/superAdmin/configCuenta.html',
                                  {'form': form, 'mensaje': 'Las contraseñas no coinciden.'})
            else:
                form = ChangePassAdminForm()
                return render(request, 'helpmapp/Administrador/superAdmin/configCuenta.html',
                              {'form': form, 'mensaje': 'La contraseña actual que ingreso es incorrecta.'})

    return render(request, 'helpmapp/Administrador/superAdmin/configCuenta.html', {'form': form})


# CREAR UNA CUENTA DE ADMINISTRADOR
def mostrar_crearAdministrador(request):
    if request.method == 'GET':
        form = AdminForm()
        return render(request, 'helpmapp/Administrador/superAdmin/crearAdmin.html', {'form': form})
    elif request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            print('si es valid')
            admin = form.save(commit=False)
            admin.save()
            return render(request, 'helpmapp/Administrador/superAdmin/crearAdmin.html', {'form': form})
        else:
            print('no es valido')
    form = AdminForm()
    return render(request, 'helpmapp/Administrador/superAdmin/crearAdmin.html', {'form': form})


def mostrar_verCentro(request, id_centro):
    if ('member_id' in list(request.session.keys())):
        if (request.session["tipo"] == 0):
            centro = CentroDeAcopio.objects.get(id=id_centro)
            if (centro):
                print("Centro encontrado")
                print(centro)
            return render(request, 'helpmapp/Administrador/superAdmin/verCentro.html', {"centro": centro})

        else:
            return HttpResponseRedirect('/administradorZonal/')
    else:
        return HttpResponseRedirect('/loginAdmin/')


def mostrar_crearProducto(request):
    if ('member_id' in list(request.session.keys())):
        if (request.session["tipo"] == 0):
            if request.method == 'POST':
                print('si es post')
                form = ProductoForm(request.POST)
                if form.is_valid():
                    print('si es valid')
                    producto = form.save(commit=False)
                    producto.save()
                    centros = CentroDeAcopio.objects.all()
                    return render(request, 'helpmapp/Administrador/superAdmin/index.html', {'centros': centros})
                else:
                    print('no es valido')
            else:
                print('no es post')
                form = ProductoForm()
            return render(request, 'helpmapp/Administrador/superAdmin/crearProducto.html', {'form': form})
        else:
            return HttpResponseRedirect('/administradorZonal/')
    else:
        return HttpResponseRedirect('/loginAdmin/')


# PÁGINAS DEL ADMINISTRADOR ZONAL
def mostrar_administradorZonal(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            print(request.session["member_id"])
            upc = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
            return render(request, 'helpmapp/Administrador/adminCentro/index.html', {'upc': upc})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')

        #     if('member_id' in list(request.session.keys())):

    return HttpResponseRedirect('/loginAdmin/')


def mostrar_configuracionCapacidades(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            if request.method == 'GET':
                form = configurarCapacidadesForm()
                return render(request, 'helpmapp/Administrador/adminCentro/configuracionCapacidades.html',
                              {'form': form})

            elif request.method == 'POST':
                form = configurarCapacidadesForm(request.POST)
                if form.is_valid():
                    print("is valid")
                    data = form.cleaned_data
                    ca = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])  # data['correo']
                    ca.almacenamiento_agua = data['almacenamiento_agua']
                    ca.almacenamiento_ropa = data['almacenamiento_ropa']
                    ca.almacenamiento_comida = data['almacenamiento_comida']
                    ca.save()
                    print(ca)
                    upc = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                    return render(request, 'helpmapp/Administrador/adminCentro/index.html', {'upc': upc})
            form = configurarCapacidadesForm()
            return render(request, 'helpmapp/Administrador/adminCentro/index.html', {'form': form})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')


def mostrar_configuracionCuenta(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            if request.method == 'GET':
                form = ChangePassAdminForm()
                return render(request, 'helpmapp/Administrador/adminCentro/configuracionCuenta.html', {'form': form})
            elif request.method == 'POST':
                form = ChangePassAdminForm(request.POST)
                if form.is_valid():
                    print("is valid")
                    data = form.cleaned_data
                    admin = Administrador.objects.get(nombre_usuario=request.session['member_id'])
                    if data['password_actual'] == admin.contrasena:
                        if data['password'] == data['confirm_password']:
                            admin.contrasena = data['password']
                            admin.save()
                            form = ChangePassAdminForm()
                            return render(request, 'helpmapp/Administrador/adminCentro/configuracionCuenta.html',
                                          {'form': form, 'mensaje': 'Su contraseña ha sido cambiada.'})
                        else:
                            form = ChangePassAdminForm()
                            return render(request, 'helpmapp/Administrador/adminCentro/configuracionCuenta.html',
                                          {'form': form, 'mensaje': 'Las contraseñas no coinciden.'})
                    else:
                        form = ChangePassAdminForm()
                        return render(request, 'helpmapp/Administrador/adminCentro/configuracionCuenta.html',
                                      {'form': form, 'mensaje': 'La contraseña actual que ingreso es incorrecta.'})

            return render(request, 'helpmapp/Administrador/adminCentro/configuracionCuenta.html', {'form': form})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')


def mostrar_inventarioAgua(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            if request.method == 'GET':
                aguas = Producto.objects.filter(id_categoria=3)
                centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                return render(request, 'helpmapp/Administrador/adminCentro/inventarioAgua.html',
                              {'aguas': aguas, 'centro': centro})
            elif request.method == 'POST':
                form = ExistenciaInventarioForm(request.POST)
                print(form)
                if form.is_valid():
                    print('si es valid')
                    inventario = form.save(commit=False)
                    inventario.save()
                    aguas = Producto.objects.filter(id_categoria=3)
                    centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                    return render(request, 'helpmapp/Administrador/adminCentro/inventarioAgua.html',
                                  {'aguas': aguas, 'centro': centro})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')


def mostrar_inventarioComida(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            if request.method == 'GET':
                comidas = Producto.objects.filter(id_categoria=1)
                centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                return render(request, 'helpmapp/Administrador/adminCentro/inventarioComida.html',
                              {'comidas': comidas, 'centro': centro})
            elif request.method == 'POST':
                form = ExistenciaInventarioForm(request.POST)
                print(form)
                if form.is_valid():
                    print('si es valid')
                    inventario = form.save(commit=False)
                    inventario.save()
                    comidas = Producto.objects.filter(id_categoria=1)
                    centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                    return render(request, 'helpmapp/Administrador/adminCentro/inventarioComida.html',
                                  {'comidas': comidas, 'centro': centro})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')


def mostrar_inventarioRopa(request):
    if ('member_id' in list(request.session.keys())):
        if ('tipo' in list(request.session.keys()) and request.session['tipo'] == 1):
            if request.method == 'GET':
                ropas = Producto.objects.filter(id_categoria=2)
                centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                return render(request, 'helpmapp/Administrador/adminCentro/inventarioRopa.html',
                              {'ropas': ropas, 'centro': centro})
            elif request.method == 'POST':
                form = ExistenciaInventarioForm(request.POST)
                print(form)
                if form.is_valid():
                    print('si es valid')
                    inventario = form.save(commit=False)
                    inventario.save()
                    ropas = Producto.objects.filter(id_categoria=2)
                    centro = CentroDeAcopio.objects.get(usuario_admin=request.session['member_id'])
                    return render(request, 'helpmapp/Administrador/adminCentro/inventarioRopa.html',
                                  {'ropas': ropas, 'centro': centro})
        if ('tipo' in list(request.session.keys())):
            return HttpResponseRedirect('/administradorGeneral/')
    return HttpResponseRedirect('/loginAdmin/')


def profile(request, nombre_usuario):
    helpmapper = get_object_or_404(HelpMapper, pk=nombre_usuario)
    return render(request, 'helpmapp/cliente/helpmapper/profile.html', {'hm': helpmapper})


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass

    return HttpResponseRedirect('/')


def mostrar_recuperarCuenta(request):
    return render(request, 'helpmapp/Administrador/superAdmin/recuperarCuenta.html')


def saveData():
    return


# Registrar helpmapper
def registrar_helpmapper(request):
    if request.method == 'POST':
        print('si es post')
        form = HelpMapperForm(request.POST)
        if form.is_valid():
            print('si es valid')
            helpmapper = form.save(commit=False)
            helpmapper.save()
            return render(request, 'helpmapp/cliente/not_logged/voluntario.html', {'form': form})
        else:
            print('no es valido')
    else:
        print('no es post')
        form = HelpMapperForm()
    return render(request, 'helpmapp/cliente/not_logged/voluntario.html', {'form': form})


def change_password(request):
    if request.method == 'GET':
        form = ChangePassForm()
        return render(request, 'helpmapp/cliente/helpmapper/change_password.html', {'form': form})

    elif request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            print("is valid")
            data = form.cleaned_data
            admin = HelpMapper.objects.get(nombre_usuario=request.session['member_id'])
            if data['password'] == data['confirm_password']:
                admin.contrasena = data['password']
                admin.save()
                form = ChangePassForm()
                return render(request, 'helpmapp/cliente/helpmapper/change_password.html',
                              {'form': form, 'mensaje': 'Su contraseña ha sido cambiada.'})
            else:
                form = ChangePassForm()
                return render(request, 'helpmapp/cliente/helpmapper/change_password.html',
                              {'form': form, 'mensaje': 'Las contraseñas no coinciden.'})

    return render(request, 'helpmapp/cliente/helpmapper/change_password.html', {'form': form})


def eliminar_helpmapper(request):
    if request.method == 'POST':
        usuario = request.session['member_id']
        del request.session['member_id']
        hm = HelpMapper.objects.get(nombre_usuario=usuario)
        helpmapper = get_object_or_404(HelpMapper, pk=hm.nombre_usuario).delete()
    return HttpResponseRedirect('/')


def obtener_datos(request):
    response_data = {}
    l = []  # diccionario que contendrá la cantidad de cada prenda de ropa
    ropa = Producto.objects.filter(id_categoria=2)  # filtro todos los productos que sean ropa
    maxropa = 0
    for r in ropa:
        prendas = ExistenciaInventario.objects.filter(
            id_producto=r.id)  # filtro todos los inventariados por cada prenda
        print(prendas)
        c = 0
        for p in prendas:
            c += int(p.cantidad)
        # c=prendas.cantidad.sum()
        if (c > maxropa):
            maxropa = c
        d = {}
        d["dept"] = r.nombre_producto
        d["age"] = c
        l.append(d)
    response_data["cantidad_ropa"] = l
    response_data["max_ropa"] = maxropa

    l2 = []
    comida = Producto.objects.filter(id_categoria=1)  # filtro todos los productos que sean comida
    maxcomida = 0
    for c in comida:
        productos = ExistenciaInventario.objects.filter(
            id_producto=c.id)  # filtro todos los inventariados por cada producto
        cantidad = 0
        for p in productos:
            cantidad += float(p.cantidad)
        # c=prendas.cantidad.sum()
        if (cantidad > maxcomida):
            maxcomida = cantidad
        d = {}
        d["dept"] = c.nombre_producto
        d["age"] = cantidad
        l2.append(d)
    response_data["cantidad_comida"] = l2
    response_data["max_comida"] = maxcomida

    l3 = []
    agua = Producto.objects.get(nombre_producto="agua")
    centros = CentroDeAcopio.objects.all()
    d = {}
    for c in centros:
        canton = c.canton
        if (canton in list(d.keys())):
            try:
                existencia = ExistenciaInventario.objects.get(id_centro=c.id, id_producto=agua.id)
                d[canton] += float(existencia.cantidad)
            except ExistenciaInventario.DoesNotExist:
                pass
        else:
            try:
                existencia = ExistenciaInventario.objects.get(id_centro=c.id, id_producto=agua.id)
                d[canton] = float(existencia.cantidad)
            except ExistenciaInventario.DoesNotExist:
                pass
    max = 0
    for k, v in d.items():
        temp = {}
        temp["dept"] = k
        temp["age"] = v
        if (v > max):
            max = v
        l3.append(temp)
    temp = {}
    temp["dept"] = "canton-prueba"
    temp["age"] = 300
    l3.append(temp)
    response_data["agua_canton"] = l3
    response_data["max_agua"] = max
    # comida=Producto.objects.filter(id_categoria=1)
    # hoy=datetime.date.today()
    # fecha=hoy-datetime.timedelta(days=7)
    # cursor=connection.cursor()
    # resultados=cursor.execute("SELECT fecha, SUM(IF(accion=\'enviar\',cantidad,0)) as \'enviar\' FROM CambioInventario,Producto WHERE CambioInventario.id_producto=Producto.id_producto and id_categoria=1 and fecha>="+fecha)
    # resultados=dictfetchall(cursor) #de la forma [{'fecha': jfahsdf,'enviar':239},{'fecha': jferwsdf,'enviar':230}]
    # response_data["comida_enviada"]=resultados
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

# def obtener_datosProvincias(request):
#     json_data = open('file:///home/helpmapp/helpmapp/static/data/provincias.json')
#     data1 = json.load(json_data)    # deserializes it
#     data2 = json.dumps(json_data)   # json formatted string

#     json_data.close()
#     return HttpResponse(
#             json.dumps(data2),
#             content_type="application/json"
#         )
