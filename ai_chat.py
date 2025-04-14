from openai import ChatCompletion

class ChatGPT:
    def __init__(self):
        self.api_key = "your_openai_api_key"
        self.model = "gpt-3.5-turbo"
    
    def generate_response(self, prompt):
        response = ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.api_key
        )
        return response.choices[0].message["content"]