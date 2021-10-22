from django.urls import path
from Control_IM.views import *


urlpatterns = [
    path(r'Create_IM/', InventarioInsumos_Create.as_view() , name="Create Inventario Alimentos"),
    path(r'List_IM/' , InventarioInsumos_List.as_view(), name="Lista de inventario alimentos"),
    path(r'ID_IM/<int:id>' , InventarioInsumos_byID.as_view(), name="List IA by id"),
    path(r'Update_IM/<int:id>', InventarioInsumos_Update.as_view(), name="Update IA"),
    path(r'Delete_IM/<int:id>', InventarioInsumos_Delete.as_view() , name="Delete IA")
]