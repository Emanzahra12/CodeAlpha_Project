import random
import time

RESPONSES = {

    "hello"         : ["Hi there! 👋", "Hello! How can I help you?", "Hey! Nice to meet you!"],
    "hi"            : ["Hi! 😊", "Hello there!", "Hey! What's up?"],
    "hey"           : ["Hey! 👋", "Hi! How are you?", "Hello!"],

    "how are you"   : ["I'm doing great, thanks for asking! 😊", "I'm fine, thank you!", "All good on my end! How about you?"],
    "how are you?"  : ["I'm doing great, thanks for asking! 😊", "I'm fine, thank you!", "All good on my end! How about you?"],


    "what is your name"  : ["I'm CodeBot 🤖, your Python chatbot!", "My name is CodeBot! Nice to meet you."],
    "what's your name"   : ["I'm CodeBot 🤖, your Python chatbot!", "My name is CodeBot! Nice to meet you."],
    "your name"          : ["I'm CodeBot 🤖!", "You can call me CodeBot!"],

    "how old are you"    : ["I was just created, so I'm very young! 😄", "Age is just a number for a bot! 🤖"],
    "how old are you?"   : ["I was just created, so I'm very young! 😄", "Age is just a number for a bot! 🤖"],

    "who made you"       : ["I was built by a CodeAlpha intern using Python! 🐍", "A Python developer created me for CodeAlpha!"],
    "who created you"    : ["I was built by a CodeAlpha intern using Python! 🐍", "A Python developer created me for CodeAlpha!"],

    "good"          : ["Thank you! 😊", "Glad to hear that!", "Great! 🎉"],
    "great"         : ["Awesome! 🎉", "That's wonderful to hear!"],
    "awesome"       : ["Thanks! You're awesome too! 😄", "Glad you think so! 🚀"],
    "thanks"        : ["You're welcome! 😊", "Happy to help!", "Anytime! 👍"],
    "thank you"     : ["You're welcome! 😊", "Happy to help!", "No problem at all!"],

    "help"          : ["Sure! You can ask me:\n  - How are you?\n  - What is your name?\n  - Tell me a joke\n  - What can you do?\n  - Bye"],
    "what can you do": ["I can chat with you, tell jokes, and answer simple questions! Try asking: 'tell me a joke' 😄"],

    "tell me a joke" : [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
        "Why did the Python programmer wear glasses? Because he couldn't C! 😂",
        "How do you comfort a JavaScript bug? You console it! 😄",
    ],
    "joke"           : [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
        "Why did the Python programmer wear glasses? Because he couldn't C! 😂",
        "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?' 😄",
    ],

    "python"        : ["Python is my favorite language too! 🐍 It's beginner-friendly and powerful!"],
    "codealpha"     : ["CodeAlpha is a great platform for internships! Keep up the hard work! 💪"],

    "bye"           : ["Goodbye! 👋 Have a great day!", "See you later! 😊", "Bye! Come back anytime! 👋"],
    "goodbye"       : ["Goodbye! 👋", "See you soon! Take care! 😊"],
    "exit"          : ["Exiting chat... Goodbye! 👋"],
    "quit"          : ["Quitting... See you next time! 👋"],
}

DEFAULT_REPLIES = [
    "Hmm, I'm not sure about that. 🤔 Try asking something else!",
    "I didn't quite understand that. Can you rephrase?",
    "Interesting! But I don't have an answer for that yet. 😅",
    "I'm still learning! Could you ask something else?",
]

def get_response(user_input):
    """Match user input to a response. Returns a string reply."""
    text = user_input.lower().strip()

    if text in RESPONSES:
        return random.choice(RESPONSES[text])

    for key in RESPONSES:
        if key in text:
            return random.choice(RESPONSES[key])


    return random.choice(DEFAULT_REPLIES)


def type_effect(message, delay=0.03):
    """Print message character by character for a typing feel."""
    print("  CodeBot: ", end="", flush=True)
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  

def main():
    print("\n" + "=" * 50)
    print("       🤖 Welcome to CodeBot Chatbot!")
    print("       Type 'bye' or 'quit' to exit.")
    print("=" * 50 + "\n")

    type_effect("Hello! I'm CodeBot 🤖. How can I help you today?")

    while True:
        try:
            user_input = input("\n  You: ").strip()

            if not user_input:
                print("  ⚠  Please type something!")
                continue

            response = get_response(user_input)
            type_effect(response)

        
            if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
                break

        except KeyboardInterrupt:
            print("\n\n  CodeBot: Goodbye! 👋\n")
            break

    print()

if __name__ == "__main__":
    main()