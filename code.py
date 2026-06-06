import datetime

# -------------------------------
# Knowledge Base
# -------------------------------
knowledge_base = {
    "python": "Python is a high-level programming language used in AI, web development, automation, and data science.",
    "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "machine learning": "Machine Learning is a subset of AI that enables systems to learn from data.",
    "chatbot": "A chatbot is a software application designed to simulate human conversation.",
    "data science": "Data Science involves extracting insights from data using statistics and machine learning."
}

# -------------------------------
# Chat History File
# -------------------------------
LOG_FILE = "chat_history.txt"

# -------------------------------
# Save Conversation
# -------------------------------
def log_conversation(user_input, bot_response):
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"\n[{timestamp}]\n")
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_response}\n")
        file.write("-" * 40 + "\n")

# -------------------------------
# Chatbot Response Function
# -------------------------------
def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    # Greetings
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]

    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    # Help Intent
    elif "help" in user_input:
        return """
I can help you with:
1. Python
2. AI
3. Machine Learning
4. Chatbot
5. Data Science

Type a topic name to know more.
"""

    # Small Talk
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot."

    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"

    # Exit
    elif user_input == "bye":
        return "Goodbye! Have a great day."

    # Knowledge Base Questions
    for topic in knowledge_base:
        if topic in user_input:
            return knowledge_base[topic]

    # Default Response
    return "Sorry, I don't understand. Type 'help' to see available options."

# -------------------------------
# Main Program
# -------------------------------
print("=" * 50)
print("      SIMPLE RULE-BASED CHATBOT")
print("=" * 50)
print("Type 'help' for options.")
print("Type 'bye' to exit.\n")

while True:

    user_message = input("You: ")

    bot_message = chatbot_response(user_message)

    print("Bot:", bot_message)

    # Save chat history
    log_conversation(user_message, bot_message)

    # Exit condition
    if user_message.lower().strip() == "bye":
        break