from rest_framework import serializers
from apps.Users.Control_Usuario.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username' , 'email' , 'name' , 'last_name']