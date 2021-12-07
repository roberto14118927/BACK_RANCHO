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
        fields = ('username', 'email', 'name', 'last_name' ,'roll' , 'is_active' , 'is_staff')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Las contraseñas no coinciden.'})
        return data


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
            'activo': instance.is_active,
            'super': instance.is_staff
        }


