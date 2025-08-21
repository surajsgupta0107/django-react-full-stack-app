from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  # to include all fields
        fields = ["id", "username", "password"]  # to include only required fields
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]  # to include only required fields
        extra_kwargs = {"author": {"read_only": True}}
