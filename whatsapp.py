class MessageProcessor:
    def __init__(self, encryptor):
        self.encryptor = encryptor
    
    def summarize_messages(self):
        # Simulated fetching messages
        messages = [
            "Meeting at 3 PM.",
            "Don't forget the project deadline tomorrow.",
            "Can we reschedule our call?"
        ]
        
        # Encrypt messages
        encrypted_messages = [self.encryptor.encrypt(msg) for msg in messages]
        
        # Decrypt and summarize
        summary = " ".join([self.encryptor.decrypt(msg) for msg in encrypted_messages])
        return summary