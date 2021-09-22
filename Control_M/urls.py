from django.urls import path, re_path
from Control_M import views


urlpatterns = [
    #views para empadre medico
    path(r'create/', views.Empadre_Create.as_view() , name='Create new empadre'),
    path(r'view_list/' , views.Empadre_List.as_view() , name ='All empadre'),
    path(r'find_id/<int:id>' , views.Empadre_ListById.as_view(), name='Empadre by id'),
    path(r'update/<int:id>' , views.Empadre_Update.as_view() , name='Update empadre'),
    path(r'delete/<int:id>' , views.Empadre_Delete.as_view() , name= 'Delete empadre'),

    #views para medico especialista
    path(r'create_tacto/', views.Medico_Create.as_view() , name='Create new tacto'),
    path(r'tacto_list/' , views.Medico_List.as_view() , name ='All tacto'),
    path(r'tacto_id/<int:id>' , views.Medico_ListById.as_view(), name='tacto by id'),
    path(r'update_tacto/<int:id>' , views.Medico_Update.as_view() , name='Update tacto'),
    path(r'delete_tacto/<int:id>' , views.Medico_Delete.as_view() , name= 'Delete tacto'),

]