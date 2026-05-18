from django.db import models
from django.conf import settings
from django.utils import timezone


class Book(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Por leer"
        READING = "reading", "Leyendo"
        FINISHED = "finished", "Terminado"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
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

    def change_status(self, new_status):
        if new_status == self.status:
            return
        if new_status == Book.Status.PENDING:
            self.started_at = None
            self.finished_at = None
        elif new_status == Book.Status.READING:
            if self.finished_at:
                self.finished_at = None
            else:
                self.started_at = timezone.now()
        elif new_status == Book.Status.FINISHED:
            if not self.started_at:
                self.started_at = timezone.now()
            self.finished_at = timezone.now()
        self.status = new_status
        self.save(update_fields=["status", "started_at", "finished_at"])
