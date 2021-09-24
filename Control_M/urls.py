from django.urls import path, re_path
from Control_M import views


urlpatterns = [
    #views para empadre medico
    path(r'create_empadre/', views.Empadre_Create.as_view() , name='Create new empadre'),
    path(r'view_list/' , views.Empadre_List.as_view() , name ='All empadre'),
    path(r'empadre_id/<int:id>' , views.Empadre_ListById.as_view(), name='Empadre by id'),
    path(r'empadre_update/<int:id>' , views.Empadre_Update.as_view() , name='Update empadre'),
    path(r'empadre_delete/<int:id>' , views.Empadre_Delete.as_view() , name= 'Delete empadre'),

    #views para medico especialista
    path(r'create_medico/', views.Medico_Create.as_view() , name='Create new medico'),
    path(r'medico_list/' , views.Medico_List.as_view() , name ='All medicos'),
    path(r'medico_id/<int:id>' , views.Medico_ListById.as_view(), name='medicos by id'),
    path(r'update_medico/<int:id>' , views.Medico_Update.as_view() , name='Update medicos'),
    path(r'delete_medico/<int:id>' , views.Medico_Delete.as_view() , name= 'Delete medicos'),

]