from rest_framework import fields, serializers
from apps.Users.Control_Usuario.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self , validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name' ,'roll' , 'is_active')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id ,
            'username': instance.username ,
            'email': instance.email ,
            'password': instance.password,
            'name': instance.name ,
            'last_name': instance.last_name,
            'roll': instance.roll,
            'activo': instance.is_active
        }


