import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provide a TestClient for making requests to the app"""
    return TestClient(app)


@pytest.fixture
def sample_email():
    """A sample email for testing"""
    return "test@mergington.edu"


@pytest.fixture
def sample_activity():
    """A sample activity name that exists in the app"""
    return "Chess Club"


@pytest.fixture
def nonexistent_activity():
    """An activity name that doesn't exist"""
    return "Nonexistent Activity"
