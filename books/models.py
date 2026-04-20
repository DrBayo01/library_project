from django.db import models
from django.conf import settings

class Book(models.Model):
    class status(models.TextChoices):
        PENDING = 'pending', 'Por leer'
        READING = 'reading', 'Leyendo'
        FINISHED = 'finished', 'Terminado'

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books',
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=status.choices,
        default=status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"