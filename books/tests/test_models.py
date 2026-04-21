import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", password="testpassword"
    )

@pytest.fixture
def book(user):
    return Book.objects.create(
        owner = user,
        title = "La espada del destino",
        author = "Andrzej Sapkowski",
        status=Book.Status.PENDING,
    )

class TestDaysReading:
    def test_returns_none_when_not_started_reading(self, book):
        assert book.days_reading() is None

    def test_counts_days_since_start_reading(self, book):
        book.started_at = timezone.now() - timezone.timedelta(days=5)
        book.save()
        assert book.days_reading() == 5

    def test_counts_days_until_finished(self, book):
        book.started_at = timezone.now() - timezone.timedelta(days=10)
        book.finished_at = timezone.now() - timezone.timedelta(days=3)
        book.status = Book.Status.FINISHED
        book.save()
        assert book.days_reading() == 7