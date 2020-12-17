from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['name', 'role', 'created_at']


class UserListSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(source = 'role.name')
    class Meta:
        model = User
        fields = '__all__'

