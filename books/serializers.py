from rest_framework import serializers
from .models import Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    days_reading = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "status",
            "started_at",
            "finished_at",
            "days_reading",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "days_reading",
            "started_at",
            "finished_at",
        ]

    def get_days_reading(self, obj):
        return obj.days_reading()
