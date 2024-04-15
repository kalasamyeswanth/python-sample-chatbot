import random

def get_response(user_input):
    user_input = user_input.lower()

    # Keywords and responses
    responses = {
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm doing well, thank you!", "I'm great, how about you?", "Feeling good, thanks!"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
        "help": ["Sure, what do you need assistance with?", "How can I assist you?", "I'm here to help!"],
        "weather": ["I'm not equipped to provide weather updates at the moment.", "You might want to check a weather website or app."],
        "joke": ["Why don't scientists trust atoms? Because they make up everything!", "I'm reading a book on anti-gravity. It's impossible to put down!", "What do you call fake spaghetti? An impasta!"],
        "age": ["I don't have an age, I'm just a chatbot!", "Age is just a number, don't you agree?"],
        "name": ["I don't have a name, but you can call me Chatbot!", "You can refer to me as your friendly chatbot!"],
        "love": ["Love is a beautiful thing!", "Love makes the world go round!"],
        "hate": ["Hate is a strong word. Let's focus on positive things instead!"],
        "exit": ["Goodbye!", "See you later!", "Come back anytime!"]
    }

    # Check if the input matches any keywords
    for keyword, possible_responses in responses.items():
        if keyword in user_input:
            return random.choice(possible_responses)

    # If no keyword is found, return a generic response
    return "I'm sorry, I didn't quite understand that."

def main():
    print("Chatbot: Hi there! How can I help you?")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
