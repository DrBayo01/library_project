from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):

        user = self.request.user
        qs = Book.objects.filter(owner=user)

        print(f"\n{'='*40}")
        print(f"[get_queryset] Usuario: {user} id={user.id}")
        print(f"[get_queryset] Autenticado: {user.is_authenticated}")
        print(f"[get_queryset] Auth method: {self.request.auth}")
        print(f"\n{'='*40}")
        print(f"[get_queryset] Query SQL: {qs.query}")
        print(f"[get_queryset] Resultados: {qs.count()} libros")

        return Book.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        print(f"\n[perform_create] Datos validados: {serializer.validated_data}")
        print(f"[perform_create] Asignado owner: {self.request.user}\n")

        serializer.save(owner=self.request.user)
    
    