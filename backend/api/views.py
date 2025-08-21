# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Note
from .serializers import NoteSerializers, UserSerializers


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]  # temporary

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]  # temporary

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
