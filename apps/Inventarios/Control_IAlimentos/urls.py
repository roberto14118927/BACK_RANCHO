from django.urls import path
from apps.Inventarios.Control_IAlimentos.views import *


urlpatterns = [
    path(r'Create_IA/', InventarioAlimentos_Create.as_view() , name="Create Inventario Alimentos"),
    path(r'List_IA/' , InventarioAlimentos_List.as_view(), name="Lista de inventario alimentos"),
    path(r'List_IA_ID/<int:id>' , InventarioAlimentos_byID.as_view(), name="List IA by id"),
    path(r'Update_IA/<int:id>', InventarioAlimentos_Update.as_view(), name="Update IA"),
    path(r'Delete_IA/<int:id>', InventarioAlimentos_Delete.as_view() , name="Delete IA")
]