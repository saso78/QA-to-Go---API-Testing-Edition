# tests/test_auth.py

import pytest
from utils.request_handler import RequestHandler

handler = RequestHandler()

@pytest.mark.skip(reason="Auth is simulated - replace with real auth API when available.")
def test_login():
    login_data = {
        "username": "testuser",
        "password": "testpass"
    }

    # Simulated login endpoint - replace with actual if available
    response = handler.post("/login", login_data)

    assert response.status_code == 200
    token = response.json().get("token")

    assert token is not None
    assert isinstance(token, str)
    print(f"✅ Auth token: {token}")
