import pytest
from app import app, db
from models import Magnitude  # Make sure this import is correct

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_get_magnitudes(client):
    response = client.get('/magnitudes')
    assert response.status_code == 200

def test_create_magnitude(client):
    data = {'magnitude': 5.5, 'description': 'Test magnitude'}
    response = client.post('/magnitudes', json=data)
    assert response.status_code == 201
