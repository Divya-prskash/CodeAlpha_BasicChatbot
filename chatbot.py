def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        ("hello", "hi", "hey", "howdy", "hiya"):
            "Hi there! How can I help you today?",
        ("how are you", "how are you doing", "how r u", "whats up", "what's up"):
            "I'm doing great, thanks for asking! How about you?",
        ("what is your name", "what's your name", "who are you", "your name"):
            "I'm CodeBot, your friendly CodeAlpha chatbot!",
        ("help", "what can you do", "commands", "options"):
            "Try saying: hello, how are you, what's your name, tell me a joke, bye.",
        ("joke", "tell me a joke", "say something funny", "make me laugh"):
            "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        ("bye", "goodbye", "see you", "exit", "quit", "cya"):
            "Goodbye! Have a great day!",
        ("thanks", "thank you", "thx", "ty"):
            "You're welcome! Anything else I can help with?",
        ("codealpha", "code alpha", "about codealpha"):
            "CodeAlpha is a leading software development company. Visit www.codealpha.tech!",
        ("python", "what is python"):
            "Python is an awesome, beginner-friendly programming language. Great choice!",
    }

    for keywords, reply in responses.items():
        if user_input in keywords:
            return reply

    for keywords, reply in responses.items():
        if any(kw in user_input for kw in keywords):
            return reply

    return "Hmm, I'm not sure about that. Type 'help' to see what I can do!"


def chatbot():
    print("=" * 45)
    print("    Welcome to CodeBot - CodeAlpha")
    print("=" * 45)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}\n")

        if any(word in user_input.lower() for word in ("bye", "goodbye", "exit", "quit", "cya")):
            break

if __name__ == "__main__":
    chatbot()
