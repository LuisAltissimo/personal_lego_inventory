import pytest
from fastapi.testclient import TestClient

from backend_lego_personal_inventory.app import app


@pytest.fixture
def client():
    return TestClient(app)
