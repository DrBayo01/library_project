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

    def change_status(self, book, status_required, new_status, date_field, error_message):

        if book.status != status_required:
            return Response(
                {"detail": error_message},
                status=status.HTTP_400_BAD_REQUEST
            )

        book.status=new_status
        setattr(book, date_field, timezone.now())
        book.save(update_fields=['status', date_field])
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
    
    @action(detail=True, methods=['post'], url_path='start')
    def start(self, request, pk=None):
        book = self.get_object()
        error_message = f"No puedes empezar un libro en estado '{book.get_status_display()}'."
        return self.change_status(book, Book.Status.PENDING, Book.Status.READING, 'started_at', error_message)
    
    @action(detail=True, methods=['post'], url_path='finish')
    def finish(self, request, pk=None):
        book = self.get_object()
        error_message = f"No puedes terminar un libro en estado '{book.get_status_display()}'."
        return self.change_status(book, Book.Status.READING, Book.Status.FINISHED, 'finished_at', error_message)