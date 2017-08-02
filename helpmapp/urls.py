from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.mostrar_indice, name='mostrar_indice'),
         url(r'^lol$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^donar/', views.donar,name="donar"),
        url(r'^estadistica/', views.estadisticas,name="estadisticas"),
        url(r'^tutoriales/', views.mostrar_tutoriales,name="mostrar_tutoriales"),
        url(r'^voluntario/', views.mostrar_voluntario,name="mostrar_voluntario"),
        url(r'^integrantes/', views.mostrar_sobreNosotros,name="mostrar_nsobreNosotros"),
        url(r'^loginAdmin/', views.mostrar_loginAdmin,name="mostrar_login"),
        url(r'^administradorGeneral/', views.mostrar_administradorGeneral,name="mostrar_administrador_general"),
        url(r'^administradorZonal/', views.mostrar_administradorZonal,name="mostrar_administrador_zonal"),

    ]
