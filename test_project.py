import pytest
from project import analyze_sentiment, get_response, format_message, save_conversation
import json
import os

def test_analyze_sentiment():
    # Test positive sentiment
    assert analyze_sentiment("I love this!")["category"] == "very positive"
    
    # Test negative sentiment
    assert analyze_sentiment("I hate this.")["category"] == "very negative"
    
    # Test neutral sentiment
    assert analyze_sentiment("The sky is blue.")["category"] == "neutral"
    
    # Test empty string
    with pytest.raises(ValueError):
        analyze_sentiment("")
    
    # Test non-string input
    with pytest.raises(ValueError):
        analyze_sentiment(123)
    
    # Test sentiment structure
    result = analyze_sentiment("Test message")
    assert "polarity" in result
    assert "subjectivity" in result
    assert "category" in result
    assert isinstance(result["polarity"], float)
    assert isinstance(result["subjectivity"], float)
    assert isinstance(result["category"], str)

def test_get_response():
    # Test all valid categories
    assert isinstance(get_response("very positive"), str)
    assert isinstance(get_response("positive"), str)
    assert isinstance(get_response("neutral"), str)
    assert isinstance(get_response("negative"), str)
    assert isinstance(get_response("very negative"), str)
    
    # Test invalid category
    with pytest.raises(ValueError):
        get_response("invalid_category")
    
    # Test non-string input
    with pytest.raises(ValueError):
        get_response(123)
    
    # Test case insensitivity
    assert get_response("VERY POSITIVE") == get_response("very positive")

def test_format_message():
    # Test basic message formatting
    result = format_message("User", "Hello")
    assert isinstance(result, dict)
    assert "timestamp" in result
    assert "speaker" in result
    assert "message" in result
    assert result["speaker"] == "User"
    assert result["message"] == "Hello"
    
    # Test with sentiment
    sentiment = {"category": "positive", "polarity": 0.5, "subjectivity": 0.5}
    result = format_message("User", "Hello", sentiment)
    assert "sentiment" in result
    assert result["sentiment"] == sentiment
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        format_message(123, "message")
    with pytest.raises(ValueError):
        format_message("User", 123)

def test_save_conversation():
    # Test valid conversation save
    conversation = [
        {"timestamp": "2024-03-21 10:00:00", "speaker": "User", "message": "Hello"},
        {"timestamp": "2024-03-21 10:00:01", "speaker": "Bot", "message": "Hi"}
    ]
    assert save_conversation(conversation, "test_chat.json") == True
    
    # Verify file contents
    with open("test_chat.json", "r") as f:
        saved_data = json.load(f)
    assert saved_data == conversation
    
    # Clean up test file
    os.remove("test_chat.json")
    
    # Test invalid input
    with pytest.raises(ValueError):
        save_conversation("not a list")
    
    # Test invalid file path
    with pytest.raises(IOError):
        save_conversation(conversation, "/invalid/path/chat.json")