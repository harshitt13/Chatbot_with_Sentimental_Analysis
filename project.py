from textblob import TextBlob
import sys
from termcolor import colored
import json
from datetime import datetime

def analyze_sentiment(text):
    """
    Analyze the sentiment of input text.
    Returns a dictionary containing polarity, subjectivity, and category.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input must be a non-empty string")
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    # Determine sentiment category
    if polarity > 0.3:
        category = "very positive"
    elif polarity > 0:
        category = "positive"
    elif polarity == 0:
        category = "neutral"
    elif polarity > -0.3:
        category = "negative"
    else:
        category = "very negative"
        
    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "category": category
    }

def get_response(sentiment_category):
    """
    Generate appropriate response based on sentiment category.
    Returns a string containing the chatbot's response.
    """
    if not isinstance(sentiment_category, str):
        raise ValueError("Sentiment category must be a string")
    
    responses = {
        "very positive": "That's wonderful to hear! Your positive energy is contagious!",
        "positive": "I'm glad you're feeling good! Keep that positive spirit!",
        "neutral": "I understand. Would you like to tell me more about that?",
        "negative": "I'm sorry you're feeling down. Would you like to talk about it?",
        "very negative": "I hear that you're going through a difficult time. I'm here to listen and support you."
    }
    
    sentiment_category = sentiment_category.lower()
    if sentiment_category not in responses:
        raise ValueError("Invalid sentiment category")
        
    return responses[sentiment_category]

def save_conversation(conversation_history, filename="chat_history.json"):
    """
    Save the conversation history to a JSON file.
    Returns True if successful, raises an exception if not.
    """
    if not isinstance(conversation_history, list):
        raise ValueError("Conversation history must be a list")
    
    try:
        with open(filename, 'w') as f:
            json.dump(conversation_history, f, indent=4)
        return True
    except Exception as e:
        raise IOError(f"Error saving conversation: {str(e)}")

def format_message(speaker, message, sentiment=None):
    """
    Format a chat message with timestamp and optional sentiment.
    Returns a dictionary containing the formatted message.
    """
    if not isinstance(speaker, str) or not isinstance(message, str):
        raise ValueError("Speaker and message must be strings")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if sentiment:
        return {
            "timestamp": timestamp,
            "speaker": speaker,
            "message": message,
            "sentiment": sentiment
        }
    return {
        "timestamp": timestamp,
        "speaker": speaker,
        "message": message
    }

def main():
    conversation_history = []
    
    # Welcome message
    print(colored("Welcome to Sentiment Analysis Chatbot!", "cyan"))
    name = input(colored("What's your name? ", "cyan")).strip()
    
    if not name:
        name = "User"
    
    print(colored(f"\nHello {name}! Type 'quit' or 'exit' to end the conversation.", "cyan"))
    print(colored("\nBot: How are you feeling today?", "green"))
    
    while True:
        try:
            # Get user input
            user_input = input(colored(f"\n{name}: ", "yellow")).strip()
            
            # Check for exit command
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(colored("\nBot: Goodbye! Take care!", "green"))
                save_conversation(conversation_history)
                print(colored("\nConversation saved to chat_history.json!", "cyan"))
                break
            
            # Analyze sentiment
            sentiment = analyze_sentiment(user_input)
            
            # Store user message
            user_message = format_message(name, user_input, sentiment)
            conversation_history.append(user_message)
            
            # Generate and display bot response
            bot_response = get_response(sentiment["category"])
            print(colored(f"\nBot: {bot_response}", "green"))
            
            # Store bot message
            bot_message = format_message("Bot", bot_response)
            conversation_history.append(bot_message)
            
            # Display sentiment analysis
            print(colored(
                f"\nSentiment Analysis: {sentiment['category'].title()} "
                f"(Polarity: {sentiment['polarity']:.2f}, "
                f"Subjectivity: {sentiment['subjectivity']:.2f})",
                "magenta"
            ))
            
        except KeyboardInterrupt:
            print(colored("\n\nChatbot terminated by user.", "red"))
            break
        except Exception as e:
            print(colored(f"\nAn error occurred: {str(e)}", "red"))
            continue

if __name__ == "__main__":
    main()