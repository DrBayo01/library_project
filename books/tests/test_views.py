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


class TestBookOwnerAssign:
    def test_owner_is_set_automatically(self, auth_client, user):
        response = auth_client.post(
            "/api/books/",
            {
                "title": "El Hobbit",
                "author": "JRR Tolkien",
            },
        )
        assert response.status_code == 201
        book = Book.objects.get(id=response.data["id"])
        assert book.owner == user

    def test_auth_user_cannot_set_owner_manually(self, auth_client, user, second_user):
        response = auth_client.post(
            "/api/books/",
            {
                "title": "El Hobbit",
                "author": "JRR Tolkien",
                "owner": second_user.id,
            },
        )
        assert response.status_code == 201
        book = Book.objects.get(id=response.data["id"])
        assert book.owner == user
