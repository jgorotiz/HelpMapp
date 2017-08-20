from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.mostrar_indice, name='mostrar_indice'),
         url(r'^lol$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^donar/', views.listar_centroAcopio,name="donar"),
        url(r'^estadistica/', views.estadisticas,name="estadisticas"),
        url(r'^tutoriales/', views.mostrar_tutoriales,name="mostrar_tutoriales"),
        url(r'^voluntario/', views.mostrar_voluntario,name="mostrar_voluntario"),
        url(r'^integrantes/', views.mostrar_sobreNosotros,name="mostrar_sobreNosotros"),
        url(r'^login/', views.mostrar_login,name="mostrar_login"),

        url(r'^listar/', views.listar_voluntario,name="listar_voluntario"),  

        url(r'^loginAdmin/', views.mostrar_loginAdmin,name="mostrar_loginAdmin"),

        #url(r'^administradorGeneral/', views.mostrar_administradorGeneral,name="mostrar_administrador_general"),
        url(r'^configuracionCapacidades/', views.mostrar_configuracionCapacidades,name="mostrar_configuracionCapacidades"),
        url(r'^configuracionCuenta/', views.mostrar_configuracionCuenta,name="mostrar_configuracionCuenta"),
        url(r'^crearProducto/', views.mostrar_crearProducto,name="mostrar_crearProducto"),
        url(r'^inventarioAgua/', views.mostrar_inventarioAgua,name="mostrar_inventarioAgua"),
        url(r'^inventarioComida/', views.mostrar_inventarioComida,name="mostrar_inventarioComida"),
        url(r'^inventarioRopa/', views.mostrar_inventarioRopa,name="mostrar_inventarioRopa"),

        #url(r'^administradorZonal/', views.mostrar_administradorZonal,name="mostrar_administrador_zonal"),
        url(r'^buscarCentroAcopio/', views.mostrar_buscarCentroAcopio,name="mostrar_buscarCentroAcopio"),
        url(r'^configCuenta/', views.mostrar_configCuenta,name="mostrar_configCuenta"),
        url(r'^crearAdmin/', views.mostrar_crearAdministrador,name="mostrar_crearAdministrador"),
        url(r'^verCentro/', views.mostrar_verCentro,name="mostrar_verCentro"),
        url(r'^admin/recuperarCuenta', views.mostrar_recuperarCuenta,name="mostrar_recuperarCuenta"),
        url(r'^recovery/', views.recovery,name="recovery"),


        #CRUD HelpMapper
        url(r'^voluntario/create/$', views.registrar_helpmapper,name='registrar_helpmapper'),
        url(r'^voluntario/edit/(?P<nombreUsuario>\w+)/$', views.actualizar_contrasena,name='actualizar_contrasena'),
        url(r'^voluntario/delete/(?P<nombreUsuario>\w+)/$', views.eliminar_helpmapper,name='eliminar_helpmapper'),
    ]
