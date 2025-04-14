from encryption import Encryptor
from ai_chat import ChatGPT
from whatsapp import MessageProcessor
from calling import CallManager
from activation import ActivationListener

def main():
    print("Welcome to Elvira - Your Personal AI Assistant!")
    
    # Initialize components
    encryptor = Encryptor()
    chat_engine = ChatGPT()
    message_processor = MessageProcessor(encryptor)
    call_manager = CallManager()
    activation_listener = ActivationListener()

    # Main loop
    while True:
        if activation_listener.is_activated():
            print("Elvira is now active.")
            user_input = input("How can I assist you? ")
            if user_input == "summarize my WhatsApp":
                summary = message_processor.summarize_messages()
                print(f"WhatsApp Summary: {summary}")
            elif user_input.startswith("call"):
                contact_name = user_input.replace("call ", "")
                call_manager.make_call(contact_name)
            else:
                response = chat_engine.generate_response(user_input)
                print(f"Elvira: {response}")

if __name__ == "__main__":
    main()