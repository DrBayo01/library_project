from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
    
    