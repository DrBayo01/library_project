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
    
    @action(detail=True, methods=['post'], url_path='start')
    def start(self, request, pk=None):
        book = self.get_object()

        if book.status != Book.Status.PENDING:
            return Response(
                {"detail": f"No puedes empezar un libro en estado '{book.get_status_display()}'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        book.status=Book.Status.READING
        book.started_at = timezone.now()
        book.save(update_fields=['status', 'started_at'])

        serializer = self.get_serializer(book)
        return Response(serializer.data)