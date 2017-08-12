from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

from .forms import *
def mostrar_indice(request):
    return render(request,'helpmapp/cliente/index.html')

def donar(request):
    return render(request,'helpmapp/cliente/donar.html')

def estadisticas(request):
    return render(request,'helpmapp/cliente/statistics.html')

def mostrar_tutoriales(request):
    return render(request,'helpmapp/cliente/tutoriales.html')

def mostrar_voluntario(request):
    return render(request,'helpmapp/cliente/voluntario.html')

def listar_voluntario(request):
    voluntarios =  AyudadorMapa.objects.all()
         
    return render(request, 'helpmapp/cliente/prueba.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        print ('si es post')
        form = VoluntaryForm(request.POST)
        if form.is_valid():
            print ('si es valid')
            voluntario = form.save(commit=False)
            voluntario.save()
            return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})
        else:
            print ('no es valido')

    else:
        print ('no es post')
        form = VoluntaryForm()

    return render(request, 'helpmapp/cliente/voluntario.html', {'form': form})




def mostrar_sobreNosotros(request):
    return render(request,'helpmapp/cliente/aboutus.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VoluntaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
                   
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
    
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            m = Administrador.objects.get(nombreUsuario=request.POST['username'])
            if m.contrasena == request.POST['password']:
                request.session['id'] = m.id_Administrador
                if (m.tipo==0): #es super admin
                    return redirect ('helpmapp/Administrador/superAdmin/index.html')
                else:#es admin de centro de acopio
                    return redirect ('helpmapp/Administrador/adminCentro/index.html')
            else:
                messages.error(request, "Credenciales incorrectas")
        else:
            messages.error(request,"Formulario no válido")
    else:
        form= LoginForm()
    return render(request,'helpmapp/Administrador/index.html',{'form': form})

#CERRAR SESIÓN DE ADMIN
def cerrarSesion(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    
    return redirect('helpmapp/Administrador/index.html')

#MOSTRAR INDEX DEL SUPER ADMIN
@login_required(login_url='/loginAdmin/')
#@permission_required('helpmapp.is_superadmin', login_url='/loginAdmin/')
def mostrar_administradorGeneral(request):
    return render(request,'helpmapp/Administrador/superAdmin/index.html')

def mostrar_administradorZonal(request):
    return render(request,'helpmapp/Administrador/adminCentro/index.html')

def mostrar_configuracionCapacidades(request):
    return render(request,'helpmapp/Administrador/adminCentro/configuracionCapacidades.html')

def mostrar_configuracionCuenta(request):
    return render(request,'helpmapp/Administrador/adminCentro/configuracionCuenta.html')

def mostrar_crearProducto(request):
    return render(request,'helpmapp/Administrador/adminCentro/crearProducto.html')

def mostrar_inventarioAgua(request):
    return render(request,'helpmapp/Administrador/adminCentro/inventarioAgua.html')

def mostrar_inventarioComida(request):
    return render(request,'helpmapp/Administrador/adminCentro/inventarioComida.html')

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

