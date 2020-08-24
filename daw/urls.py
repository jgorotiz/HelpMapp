from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Examples:
    # url(r'^$', 'daw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('',include(('helpmapp.urls','helpmapp'), namespace='helpmapp'))
]
