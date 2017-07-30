from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.mostrar_indice, name='mostrar_indice'),
         url(r'^lol$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^donar/', views.donar,name="donar"),
        url(r'^estadistica/', views.estadisticas,name="estadisticas"),
        url(r'^tutoriales/', views.mostrar_tutoriales,name="mostrar_tutoriales"),

    ]
