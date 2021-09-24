from django.urls import path, re_path
from Control_T import views

urlpatterns = [
    path(r'create/', views.Empadre_Create.as_view() , name='Create new empadre termo'),
    path(r'view_list/' , views.Empadre_List.as_view() , name ='All empadre termo'),
    path(r'find_id/<int:id>' , views.Empadre_ListById.as_view(), name='Empadre by id termo'),
    path(r'update/<int:id>' , views.Empadre_Update.as_view() , name='Update empadre termo'),
    path(r'delete/<int:id>' , views.Empadre_Delete.as_view() , name= 'Delete empadre termo'),

    path(r'create_termo/', views.Termo_Create.as_view() , name='Create new termo'),
    path(r'termo_list/' , views.Termo_List.as_view() , name =('All termo')),
    path(r'termo_id/<int:id>' , views.Termo_ListById.as_view(), name='Termo by id'),
    path(r'update_termo/<int:id>' , views.Termo_Update.as_view() , name='Update termo'),
    path(r'delete_termo/<int:id>' , views.Termo_Delete.as_view() , name= 'Delete termo'),

]