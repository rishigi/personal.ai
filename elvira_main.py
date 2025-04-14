import encryption
import ai_chat
import whatsapp
import calling
import activation

def main():
    print("Welcome to Elvira - Your Personal AI Assistant!")
    
    # Initialize AI Chat
    chat_engine = ai_chat.ChatGPT()
    
    # Initialize Encryption
    encryptor = encryption.Encryptor()
    
    # Activation Listener
    activation_listener = activation.ActivationListener()
    
    # WhatsApp Message Summarization
    message_processor = whatsapp.MessageProcessor(encryptor)
    
    # Calling Functionality
    call_manager = calling.CallManager()
    
    # Main event loop
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