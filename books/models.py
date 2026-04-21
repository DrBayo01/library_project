from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    class Status(models.TextChoices):
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
        choices=Status.choices,
        default=Status.PENDING
    )
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    
    def days_reading(self):
        if not self.started_at:
            return None
        end = self.finished_at or timezone.now()
        return (end - self.started_at).days