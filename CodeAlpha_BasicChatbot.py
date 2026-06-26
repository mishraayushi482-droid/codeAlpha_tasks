def ChatBot_Response(User_Input):
    User_Input= User_Input.lower().strip()

    if "hello" in User_Input:
        return "Hi!"
    elif "how are you" in User_Input:
        return "I'm fine, thanks!"
    elif "bye" in User_Input:
        return "Goodbye!"
    else:
        return "Hey! I am A Simple Chatbot. Try Saying 'hello', 'how are you', or 'bye'"

def Start_Chatbot():
        print("Chatbot: Hey! I am Your Assistant. Type 'bye' to exit")

        while True:
            User_Text= input("You: ")

            Response= ChatBot_Response(User_Text)
            print("Chatbot:", Response)
            if "bye" in User_Text.lower():
                break

if __name__ == "__main__":
    Start_Chatbot()
