from django.urls import path
from apps.Inventarios.Control_IMateriales.views import *


urlpatterns = [
    path(r'Create_IMA/', InventarioMateriales_Create.as_view() , name="Create Inventario Alimentos"),
    path(r'List_IMA/' , InventarioMateriales_List.as_view(), name="Lista de inventario alimentos"),
    path(r'ID_IMA/<int:id>' , InventarioMateriales_byID.as_view(), name="List IA by id"),
    path(r'Update_IMA/<int:id>', InventarioMateriales_Update.as_view(), name="Update IA"),
    path(r'Delete_IMA/<int:id>', InventarioMateriales_Delete.as_view() , name="Delete IA")
]