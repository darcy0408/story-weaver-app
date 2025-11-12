from app import Character, db
import uuid

def test_character_creation(client):
    """Test Character model creation"""
    with client.application.app_context():
        char = Character(
            id=str(uuid.uuid4()),
            name='Test',
            age=7,
            gender='Girl'
        )
        db.session.add(char)
        db.session.commit()

        # Retrieve
        found = Character.query.filter_by(name='Test').first()
        assert found is not None
        assert found.age == 7

def test_character_to_dict(client):
    """Test Character.to_dict() method"""
    with client.application.app_context():
        char = Character(
            id=str(uuid.uuid4()),
            name='Test',
            age=7,
            gender='Girl',
            personality_sliders={'sociability': 75}
        )
        data = char.to_dict()
        assert data['name'] == 'Test'
        assert data['personality_sliders']['sociability'] == 75
