from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.show_index, name='show_index'),
         url(r'^lol$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),

    ]
