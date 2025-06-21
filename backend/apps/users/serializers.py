# backend/apps/users/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Define os campos que a API vai aceitar para criar um usuário
        fields = ['id', 'username', 'email', 'password']
        # Garante que a senha seja usada para escrever, mas não para ler
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Nós sobrescrevemos o método create padrão para usar o create_user do Django.
        # Isso é CRUCIAL para garantir que a senha seja corretamente "hasheada" (criptografada)
        # antes de ser salva no banco de dados.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user