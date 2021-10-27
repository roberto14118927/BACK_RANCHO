from django.urls import path, re_path
from apps.Ganado.Control_Peso import views


urlpatterns = [
    #urls para el peso
    path(r'create/' , views.Peso_Create.as_view() , name=("Create new weithg")),
    path(r'view_list/' , views.Peso_List.as_view() , name ='All pesos'),
    path(r'find_id/<int:id>' , views.PesoList_By_Id.as_view(), name='Pesos by id'),
    path(r'find_idG/<int:id>', views.PesoList_By_IdGanado.as_view() , name ="Peso por id ganado"),
    path(r'update/<int:id>' , views.Peso_Update.as_view() , name='Update Peso'),
    path(r'delete/<int:id>' , views.Peso_Delete.as_view() , name= 'Delete Peso'),


    #urls para las enfermedades
    path(r'create_enf/' , views.Enfermedad_Create.as_view() , name=("Create new enf")),
    path(r'list_enf/' , views.Enfermedades_List.as_view() , name=("All enf")),
    path(r'list_id/<int:id>' , views.Enfermedades_List_By_Id.as_view() , name=("enf by id")),
    path(r'update_enf/<int:id>' , views.Enfermedad_Update.as_view() , name=("Update enf")),
    path(r'delete_enf/<int:id>' , views.Enfermedad_Delete.as_view() , name=("Delete enf")),

    #urls para asociación
    path(r'create_aso/' , views.Asociacion_Create.as_view() , name=("Create new aso")),
    path(r'list_aso/' , views.Asociation_List.as_view() , name=("All aso")),
    path(r'list_aso_id/<int:id>' , views.Asociaciones_List_By_Id.as_view() , name=("aso by id")),
    path(r'list_aso_enf/<int:id>', views.Asociaciones_List_By_enfermedad.as_view() ,name=("Aso by id enfermedad")),
    path(r'update_aso/<int:id>' , views.Asociacion_Update.as_view() , name=("Update asociacion")),
    path(r'delete_aso/<int:id>' , views.Asociacion_Delete.as_view() , name=("Delete asociacion")),
]