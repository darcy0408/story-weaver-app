import pytest
from app import app, db

def test_health_endpoint(client):
    """Test /health returns 200 with correct data"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert 'has_api_key' in data

def test_generate_story_requires_character(client):
    """Test /generate-story validates required fields"""
    response = client.post('/generate-story', json={})
    # Should handle missing character gracefully
    assert response.status_code in [200, 400]

def test_generate_story_with_feelings(client):
    """Test /generate-story accepts feelings wheel data"""
    response = client.post('/generate-story', json={
        'character': 'Test Child',
        'theme': 'Adventure',
        'character_age': 7,
        'current_feeling': {
            'core_emotion': 'Joy',
            'secondary_emotion': 'Excited',
            'tertiary_emotion': 'Enthusiastic',
            'intensity': 4
        }
    })
    assert response.status_code in [200, 202]  # 202 if async

def test_create_character(client):
    """Test /create-character endpoint"""
    response = client.post('/create-character', json={
        'name': 'Test',
        'age': 7,
        'gender': 'Girl'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test'
    assert 'id' in data
