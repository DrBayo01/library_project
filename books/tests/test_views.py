import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from books.models import Book

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpassword")


@pytest.fixture
def second_user(db):
    return User.objects.create_user(username="testuser2", password="testpassword")


@pytest.fixture
def auth_client(user):
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.fixture
def book(user):
    return Book.objects.create(
        owner=user,
        title="La espada del destino",
        author="Andrzej Sapkowski",
        status=Book.Status.PENDING,
    )


@pytest.fixture
def second_book(second_user):
    return Book.objects.create(
        owner=second_user,
        title="The Final Empire",
        author="Brandon Sanderson",
        status=Book.Status.PENDING,
    )


class TestBookIsolation:
    def test_user_only_can_see_own_books(self, auth_client, book, second_book):
        response = auth_client.get("/api/books/")

        ids = [b["id"] for b in response.data]

        assert book.id in ids
        assert second_book.id not in ids

    def test_user_cannot_access_other_book(self, auth_client, second_book):
        response = auth_client.get(f"/api/books/{second_book.id}/")
        assert response.status_code == 404


class TestStartAction:

    def cannot_start_assert(self, status, auth_client, book):
        book.status = status
        book.save()

        response = auth_client.post(f"/api/books/{book.id}/start/")
        assert response.status_code == 400

    def test_start_pending_book(self, auth_client, book):
        response = auth_client.post(f"/api/books/{book.id}/start/")
        assert response.status_code == 200
        assert response.data["status"] == "reading"
        assert response.data["started_at"] is not None

    def test_cannot_start_already_reading(self, auth_client, book):
        self.cannot_start_assert(Book.Status.READING, auth_client, book)

    def test_cannot_start_finished_book(self, auth_client, book):
        self.cannot_start_assert(Book.Status.FINISHED, auth_client, book)

    def test_cannot_start_other_users_book(self, auth_client, second_book):
        response = auth_client.post(f"/api/books/{second_book.id}/start/")
        assert response.status_code == 404
