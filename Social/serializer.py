from rest_framework import routers, serializers, viewsets

from Social.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ('__all__')