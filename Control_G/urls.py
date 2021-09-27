from django.urls import path, re_path 
from rest_framework import routers
from Control_G import views

urlpatterns = [
    #paths para ganado
    path(r'create/', views.GanadoCreate.as_view() , name='Create new cow'),
    path(r'view_list/' , views.GanadoList.as_view() , name ='All cows'),
    path(r'find_id/<int:id>' , views.GanadoListById.as_view(), name='Cows by id'),
    path(r'update/<int:id>' , views.GanadoUpdate.as_view() , name='Update cow'),
    path(r'delete/<int:id>' , views.GanadoDelete.as_view() , name= 'Delete user'),

    #paths para raza
    path(r'create_raza/' , views.RazaCreate.as_view() , name="Create raza"),
    path(r'list_razas/' , views.RazaList.as_view() , name="List raza"),
    path(r'list_id/<int:id>' , views.RazaListById.as_view() , name='List raza id'),
    path(r'update_raza/<int:id>' , views.RazaUpdate.as_view() , name='Update raza'),
    path(r'delete_raza/<int:id>' , views.RazaDelete.as_view() , name= 'Delete raza'),
]