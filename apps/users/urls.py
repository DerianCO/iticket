from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.users.views import Profile

urlpatterns = [
    #url(r'^$',  index, name='index'),
    #url(r'^$', login_required(Profile), name='home'),
    url(r'^(?P<username>\w+)$', login_required(Profile), name='home'),

    #url(r'^edit/(?P<pk>\d+)/$', ProfileUpdate.as_view(), name= 'edit'),
    #url(r'^nuevo$', mascota_view, name='mascota_crear'), #Basada en funciones
    #url(r'^create$',login_required(EventCreate.as_view()) , name='events_create'), #Basada en Clases
    #url(r'^view/(?P<view>\w+)/(?P<idevent>\d+)/$', EventView, name='event_view_home'), #Basada en funciones
    #url(r'^listar$', mascota_list, name='mascota_listar'), #Basada en funciones
    #url(r'^listar$', login_required(MascotaList.as_view()), name='mascota_listar'), #Basada en clases pero sin paginacion
    #url(r'^listar', MascotaList.as_view(), name='mascota_listar'), #Basada en clases
    #url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'), #Basada en funciones
    #url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'), #Basada en clases
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'), #Basada en funciones
    #url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'), #Basada en clases
    #url(r'^listado$',listado , name='listado'), #Basada en Clases
]

