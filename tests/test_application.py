import pytest


class TestApplication:
    @pytest.fixture
    def app(self, app_with_mongomock):
        return app_with_mongomock

    def test_home(self, app):
        client = app.test_client()
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Welcome to the User API"

    def test_create_user(self, app):
        client = app.test_client()
        user_data = {"name": "John Doe", "email": "johndoe@example.com"}
        response = client.post("/users", json=user_data)
        assert response.status_code == 201
        assert response.get_json() == {"message": "User created successfully"}

    def test_get_users(self, app):
        client = app.test_client()
        response = client.get("/users")
        assert response.status_code == 200
