from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(owner=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    def perform_update(self, serializer):
        new_status = serializer.validated_data.get("status")
        if new_status:
            serializer.instance.change_status(new_status)
        serializer.save()
