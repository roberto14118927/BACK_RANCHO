from django.urls import path, re_path
from Social import views

urlpatterns = [
    path(r'create_user/', views.ProfileCreate.as_view() , name='Create user'),
    path(r'view_list/' , views.ProfileList.as_view() , name ='All users'),
    path(r'find_id/<int:id>' , views.ProfileListById.as_view(), name='Users by id'),
    path(r'update_user/<int:id>' , views.ProfileUpdate.as_view() , name='Update user'),
    path(r'delete_user/<int:id>' , views.ProfileDelete.as_view() , name= 'Delete user')
]