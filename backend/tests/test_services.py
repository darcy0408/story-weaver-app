from app import _extract_current_feeling, _build_feelings_prompt

def test_extract_feeling_handles_feelings_wheel():
    """Test feelings wheel data is parsed correctly"""
    payload = {
        'current_feeling': {
            'core_emotion': 'Sad',
            'secondary_emotion': 'Lonely',
            'tertiary_emotion': 'Isolated',
            'intensity': 3
        }
    }
    result = _extract_current_feeling(payload)
    assert result is not None
    assert result['emotion_name'] == 'Isolated'
    assert result['intensity'] == 3

def test_extract_feeling_handles_legacy_format():
    """Test old emotion format still works"""
    payload = {
        'current_feeling': {
            'emotion_name': 'Happy',
            'emotion_emoji': '😊',
            'intensity': 4
        }
    }
    result = _extract_current_feeling(payload)
    assert result is not None
    assert result['emotion_name'] == 'Happy'

def test_build_feelings_prompt():
    """Test feelings prompt generation"""
    feeling = {
        'emotion_name': 'Worried',
        'emotion_emoji': '😰',
        'intensity': 4,
        'what_happened': 'Test tomorrow'
    }
    prompt = _build_feelings_prompt('Emma', feeling)
    assert 'Emma' in prompt
    assert 'Worried' in prompt or 'worried' in prompt
    assert 'Test tomorrow' in prompt
