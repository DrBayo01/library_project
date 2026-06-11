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


class TestStatusChange:
    def test_pending_to_reading_assigns_started_at(self, auth_client, book):
        response = auth_client.patch(f"/api/books/{book.id}/", {"status": "reading"})
        assert response.status_code == 200
        assert response.data["status"] == "reading"
        assert response.data["started_at"] is not None
        assert response.data["finished_at"] is None

    def test_reading_to_finished_assigns_finished_at(self, auth_client, book):
        book.change_status(Book.Status.READING)
        response = auth_client.patch(f"/api/books/{book.id}/", {"status": "finished"})
        assert response.status_code == 200
        assert response.data["status"] == "finished"
        assert response.data["started_at"] is not None
        assert response.data["finished_at"] is not None

    def test_finished_to_reading_resets_finished_at(self, auth_client, book):
        book.change_status(Book.Status.FINISHED)
        response = auth_client.patch(f"/api/books/{book.id}/", {"status": "reading"})
        assert response.status_code == 200
        assert response.data["status"] == "reading"
        assert response.data["started_at"] is not None
        assert response.data["finished_at"] is None

    def test_change_any_status_to_pending_clears_dates(self, auth_client, book):
        book.change_status(Book.Status.READING)
        response = auth_client.patch(f"/api/books/{book.id}/", {"status": "pending"})
        assert response.status_code == 200
        assert response.data["status"] == "pending"
        assert response.data["started_at"] is None
        assert response.data["finished_at"] is None

    def test_same_status_changes_nothing(self, auth_client, book):
        response = auth_client.patch(f"/api/books/{book.id}/", {"status": "pending"})
        assert response.status_code == 200
        assert response.data["started_at"] is None

    def test_cannot_change_other_users_book_status(self, auth_client, second_book):
        response = auth_client.patch(
            f"/api/books/{second_book.id}/", {"status": "reading"}
        )
        assert response.status_code == 404


class TestBookFilter:
    def test_filter_by_status(self, auth_client, book):
        response = auth_client.get("/api/books/?status=pending")
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_filter_by_non_existing_status(self, auth_client, book):
        response = auth_client.get("/api/books/?status=literally_non_existing_status")
        assert response.status_code == 400

    def test_filter_by_status_with_no_books(self, auth_client, book):
        response = auth_client.get("/api/books/?status=finished")
        assert response.status_code == 200
        assert len(response.data) == 0

class TestCiValidation:
    def test_ci_check_validation():
        assert 1 == 2