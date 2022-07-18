import openai

class GPT3_Client:
    
    def __init__(self, key):
        self.openai.api_key = key
    
    def chat(self, message):
        openai.api_key = self.token
        completion = openai.Completion.create(
            engine="curie", 
            prompt = message,
            temperature=0.4,
            stop=['\nHuman'],
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.1,
            best_of=1
            )

        response = completion.choices[0].text.strip()
        print(f"response is : {response}")
        return response
        
    