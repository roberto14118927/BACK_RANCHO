from django.urls import path, re_path
from apps.Ganado.Control_Peso.api.views.views import PesoList_By_IdGanado , Asociaciones_List_By_enfermedad


urlpatterns = [
    #urls para el peso
    path(r'peso-ganado-id/<int:id>', PesoList_By_IdGanado.as_view() , name ="Peso por id ganado"),
    
    #urls para asociación
    path(r'aso-enfermedad-id/<int:id>', Asociaciones_List_By_enfermedad.as_view() ,name=("Aso by id enfermedad")),

]