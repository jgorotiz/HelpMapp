from django.conf.urls import include, url

from . import views
urlpatterns = [
        #For Everyone
        url(r'^$', views.mostrar_indice, name='mostrar_indice'),
        #url(r'^lol$', views.get_name),
        #url(r'^thanks/', views.show_name),
        url(r'^donar/', views.listar_centroAcopio,name="listar_centroAcopio"),
#        url(r'^voluntario/', views.mostrar_voluntario,name="mostrar_voluntario"),
        url(r'^equipo/', views.mostrar_sobreNosotros,name="mostrar_sobreNosotros"),
        url(r'^login/', views.mostrar_login,name="mostrar_login"),
        url(r'^recovery/', views.recovery,name="recovery"),

        #For HelpMapper
        url(r'^home/', views.index_hm,name="home"),
        url(r'^hm/donar/', views.listar_centroAcopioHM,name="donarHM"),
        url(r'^hm/estadistica/', views.mostrar_GraficoEstadistico,name="mostrar_GraficoEstadistico"),
        url(r'^hm/tutoriales/', views.mostrar_tutoriales,name="mostrar_tutoriales"),
        url(r'^hm/equipo/', views.mostrar_sobreNosotrosHM,name="mostrar_sobreNosotrosHM"),
        url(r'^newPassword/', views.change_password,name="cambiar_password"),
        
        
        

        url(r'^listar/', views.listar_voluntario,name="listar_voluntario"),  

        url(r'^loginAdmin/', views.mostrar_loginAdmin,name="mostrar_loginAdmin"),

        url(r'^administradorGeneral/$', views.mostrar_administradorGeneral,name="mostrar_administradorGeneral"),
        url(r'^administradorGeneral/buscarCentroAcopio/$', views.buscarCentroAcopio),
        url(r'^administradorGeneral/configuracionCuenta/$', views.mostrar_configCuenta,name="mostrar_configCuenta"),
        url(r'^administradorGeneral/crearAdmin/$', views.mostrar_crearAdministrador,name="mostrar_crearAdministrador"),
        url(r'^administradorGeneral/verCentro/(?P<id_centro>\d+)/$', views.mostrar_verCentro,name="mostrar_verCentro"),
        url(r'^administradorGeneral/crearProducto/$', views.mostrar_crearProducto,name="mostrar_crearProducto"),        



        url(r'^administradorZonal/configuracionCapacidades/', views.mostrar_configuracionCapacidades,name="mostrar_configuracionCapacidades"),
        url(r'^administradorZonal/configuracionCuenta/', views.mostrar_configuracionCuenta,name="mostrar_configuracionCuenta"), # de admin zonal
       
        url(r'^administradorZonal/inventarioAgua/', views.mostrar_inventarioAgua,name="mostrar_inventarioAgua"),
        url(r'^administradorZonal/inventarioComida/', views.mostrar_inventarioComida,name="mostrar_inventarioComida"),
        url(r'^administradorZonal/inventarioRopa/', views.mostrar_inventarioRopa,name="mostrar_inventarioRopa"),

        url(r'^administradorZonal/', views.mostrar_administradorZonal,name="mostrar_administrador_zonal"),
       
        url(r'^admin/recuperarCuenta', views.mostrar_recuperarCuenta,name="mostrar_recuperarCuenta"),

        url(r'^profile/(?P<nombre_usuario>\S+)$', views.profile),
        url(r'^logout/', views.logout,name="logout"),
        
        url(r'^cerrarSesion/', views.cerrarSesion,name="cerrarSesion"),



        #CRUD HelpMapper
        url(r'^voluntario/$', views.registrar_helpmapper,name='registrar_helpmapper'),
        #url(r'^voluntario/change_pass/$', views.actualizar_contrasena,name='actualizar_contrasena'),
        url(r'^voluntario/delete/$', views.eliminar_helpmapper,name='eliminar_helpmapper'),

        #Datos para graficos D3JS
        url(r'^datos/$', views.obtener_datos,name='obtener_datos'),

        #Datos para provincias
        #url(r'^datosProvincias/$', views.obtener_datosProvincias,name='obtener_datosProvincias'),
    ]
