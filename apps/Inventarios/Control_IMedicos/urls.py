from django.urls import path
from apps.Inventarios.Control_IMedicos.views import *


urlpatterns = [
    path(r'Create_IM/', InventarioInsumos_Create.as_view()),
    path(r'List_IM/' , InventarioInsumos_List.as_view()),
    path(r'ID_IM/<int:id>' , InventarioInsumos_byID.as_view()),
    path(r'Update_IM/<int:id>', InventarioInsumos_Update.as_view()),
    path(r'Delete_IM/<int:id>', InventarioInsumos_Delete.as_view())
]