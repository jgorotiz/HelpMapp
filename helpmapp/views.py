from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import VoluntaryForm
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

def mostrar_administradorGeneral(request):
    return render(request,'helpmapp/Administrador/superAdmin/index.html')

def mostrar_administradorZonal(request):
    return render(request,'helpmapp/Administrador/adminCentro/index.html')

def mostrar_loginAdmin(request):
    return render(request,'helpmapp/Administrador/index.html')

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

def mostrar_crearAdministrador(request):
    return render(request,'helpmapp/Administrador/superAdmin/crearAdmin.html')

def mostrar_verCentro(request):
    return render(request,'helpmapp/Administrador/superAdmin/verCentro.html')

def saveData():
    return