from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.show_index),
        # url(r'^$', views.get_name),

#        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),
        url(r'^thanks/', views.show_name),

    ]
