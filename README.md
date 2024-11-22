# Sentiment Analysis Chatbot
#### Video Demo: https://youtu.be/9veYppxT4Js
#### Description:

The Sentiment Analysis Chatbot is a Python-based interactive chat application that analyzes the emotional tone of user messages in real-time. This project was created as a final submission for Harvard's CS50P course, combining natural language processing with user interaction to create an engaging and insightful chatting experience.

### Key Features:

1. **Sentiment Analysis**
   - Analyzes text for emotional tone using TextBlob library
   - Provides detailed sentiment scores (polarity and subjectivity)
   - Categorizes messages into five sentiment levels:
     - Very Positive
     - Positive
     - Neutral
     - Negative
     - Very Negative

2. **Interactive Chat Interface**
   - Color-coded messages for better readability
   - Real-time feedback on sentiment analysis
   - User-friendly command system
   - Personalized interaction with user name

3. **Conversation Management**
   - Automatic saving of chat history to JSON
   - Timestamps for all messages
   - Structured conversation data format
   - Error handling for data saving

### Technical Implementation:

The project is structured into several key Python files:

1. **project.py**
   - Contains the main application logic
   - Implements core functions:
     - `analyze_sentiment()`: Processes text and returns sentiment metrics
     - `get_response()`: Generates contextual responses based on sentiment
     - `format_message()`: Structures messages with metadata
     - `save_conversation()`: Handles conversation persistence
   - Features comprehensive error handling

2. **test_project.py**
   - Contains pytest-compatible test functions
   - Covers all core functionalities
   - Includes edge cases and error conditions
   - Ensures code reliability

3. **requirements.txt**
   - Lists all necessary Python packages:
     - textblob: For sentiment analysis
     - termcolor: For colored console output
     - pytest: For running tests

### How to Use:

1. **Installation**
   ```bash
   pip install -r requirements.txt
   ```

2. **Running the Program**
   ```bash
   python project.py
   ```

3. **Running Tests**
   ```bash
   pytest test_project.py
   ```

4. **Basic Commands**
   - Type any message to chat
   - Use 'quit', 'exit', 'bye', or 'goodbye' to end the conversation
   - Press Ctrl+C for emergency exit

### Design Choices:

1. **TextBlob for Sentiment Analysis**
   - Chosen for its accuracy and ease of use
   - Provides both polarity and subjectivity scores
   - Well-documented and maintained library

2. **Color-Coded Interface**
   - Green: Bot messages
   - Yellow: User messages
   - Cyan: System messages
   - Magenta: Sentiment analysis results

3. **JSON for Data Storage**
   - Human-readable format
   - Easy to process and analyze
   - Maintains message structure

4. **Modular Function Design**
   - Separate functions for distinct responsibilities
   - Easy to test and maintain
   - Follows Python best practices

### Future Improvements:

1. **Enhanced Analysis**
   - Emotion detection
   - Language detection
   - Topic analysis

2. **Data Analysis**
   - Sentiment trending over time
   - User interaction patterns
   - Response effectiveness metrics

This project demonstrates the practical application of natural language processing in creating interactive systems, while maintaining code quality through comprehensive testing and error handling. It serves as both a functional chat application and an educational tool for understanding sentiment analysis in text.