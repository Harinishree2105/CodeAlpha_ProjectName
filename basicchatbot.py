
def chatbot():
    print("🤖 Chatbot: Hello! I’m your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("🤖 Chatbot: Hi! How are you?")
        elif user_input in ["i'm fine", "i am fine", "fine"]:
            print("🤖 Chatbot: Great to hear that!")
        elif user_input in ["how are you", "how are you?"]:
            print("🤖 Chatbot: I'm doing well, thank you!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn’t understand that.")


chatbot()
