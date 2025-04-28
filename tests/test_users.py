import pytest
from utils.request_handler import RequestHandler

handler = RequestHandler()

def test_get_all_users():
    response = handler.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    print("\n🧑 List of Users:")
    for user in users:
        print(f"- {user['id']}: {user['name']} ({user['email']})")

def test_get_single_user():
    response = handler.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "name" in user

