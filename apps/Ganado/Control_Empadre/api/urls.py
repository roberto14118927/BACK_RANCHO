from django.urls import path, re_path
from apps.Ganado.Control_Empadre.api.views.views import Tacto_by_id_empadre


urlpatterns = [
    path(r'tacto/empadre-id/<int:id>' , Tacto_by_id_empadre.as_view(), name='tacto by id'),
]