from django.urls import path, re_path
from Control_P import views


urlpatterns = [
    #urls para el peso
    path(r'create/' , views.Peso_Create.as_view() , name=("Create new weithg")),
    path(r'view_list/' , views.Peso_List.as_view() , name ='All cows'),
    path(r'find_id/<int:id>' , views.PesoList_By_Id.as_view(), name='Cows by id'),
    path(r'update/<int:id>' , views.Peso_Update.as_view() , name='Update cow'),
    path(r'delete/<int:id>' , views.Peso_Delete.as_view() , name= 'Delete user'),


    #urls para las enfermedades
    path(r'create_enf/' , views.Enfermedad_Create.as_view() , name=("Create new enf")),
    path(r'list_enf/' , views.Enfermedades_List.as_view() , name=("All enf")),
    path(r'list_id/<int:id>' , views.Enfermedades_List_By_Id.as_view() , name=("enf by id")),
    path(r'update_enf/<int:id>' , views.Enfermedad_Update.as_view() , name=("Update enf")),
    path(r'delete_enf/<int:id>' , views.Enfermedad_Delete.as_view() , name=("Delete enf")),

    #urls para asociación
    path(r'create_aso/' , views.Asociacion_Create.as_view() , name=("Create new aso")),
    path(r'list_aso/' , views.Asociation_List.as_view() , name=("All aso")),
    path(r'list_id/<int:id>' , views.Asociaciones_List_By_Id.as_view() , name=("aso by id")),
]