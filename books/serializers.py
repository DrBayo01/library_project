from rest_framework import serializers
from .models import Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    days_reading = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'status', 'started_at', 'finished_at', 'days_reading', 'created_at']
        read_only_fields = ['id', 'created_at', 'days_reading']

    def get_days_reading(self, obj):
        return obj.days_reading()
    
    def validate_status(self, value):
        print(f"\n[validate_status] Valor recibido: {value}")
        return value
  
    def validate(self, attrs):
        print(f"\n[validate] datos recibidos con attrs: {attrs}")

        instance = self.instance
        print(f"[validate] instance: {instance}")
        if instance:
            current_status = instance.status
        else:
            current_status = None
        new_status = attrs.get('status', current_status)
  
        print(f"[validate] Transición: {current_status} → {new_status}")

        # no se puede marcar como terminado un libro que no se empezó a leer
        if new_status == Book.Status.FINISHED:
            current_started = getattr(instance, 'started_at', None)
            new_started = attrs.get('started_at', current_started)
            print(f"[validate] current_started: {current_started}, new_started: {new_started}")
            if not new_started:
                raise serializers.ValidationError({"status": "No puedes marcar un libro como terminado sin haberlo empezado."})
            
        # si el status cambia a reading, se registra started_at automaticamente
        if new_status == Book.Status.READING and current_status == Book.Status.PENDING:
            if not attrs.get('started_at'):
                attrs['started_at'] = timezone.now()
                print(f"[validate] started_at asignado automaticamente: {attrs['started_at']}")

        # si el status cambia a finished, registra finished_at automaticamente
        if new_status == Book.Status.FINISHED and current_status != Book.Status.FINISHED:
            if not attrs.get('finished_at'):
                attrs['finished_at'] = timezone.now()
                print(f"[validate] finished_at asignado automaticamente: {attrs['finished_at']}")
        return attrs
