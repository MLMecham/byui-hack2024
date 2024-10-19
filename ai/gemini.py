import os
import google.generativeai as genai
# pip install -q -U google-generativeai

from dotenv import load_dotenv
# pip install python-dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
  }

class GeminiAI:
  
  def __init__(self, model_name):
    self.model_name = model_name
    self.api_key = os.getenv("GEMINI_API_KEY")
    self.history = []
    
    genai.configure(api_key=self.api_key)
    
    self.model = genai.GenerativeModel(self.model_name)
  
    self.generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
  
  def generate_chat(self):
    
    i = 0
    print(f"PT: How can I help you today?\n")
    
    while i != 1: # change the condition  to break the loop when user wants to exit
      self.user_input = input("You: ")
      
      if self.user_input != "quit":
        chat_session = self.model.start_chat(history=self.history)
        response = chat_session.send_message(self.user_input)
        
        self.model_response =  response.text
        print(f'Bot: {self.model_response}\n')
        
      else:
        i == 1
  
  def append_chat_to_history(self):
  
    self.history.append({"role": "user", "parts": [self.user_input]}) # The format is dictionary
    self.history.append({"role": "user", "parts": [self.model_response]}) # The format is dictionary
    
  def change_model_name(self):
    new_model_name = input("Enter the new model name: ")
    self.model_name = new_model_name

  def change_api_key(self):
    new_api_key = input("Enter the new API key: ")
    self.api_key = os.getenv(new_api_key)
  
  def single_message(self, message):
    """ Gets a single request from the genai API.
        args():
        message (string): What you will ask the AI.
        returns:
          response (string): Returns the response from the AI.
    """
    chat_session = self.model.start_chat(history=[])
    response = chat_session.send_message(message)
    return response.text


# model = genai.GenerativeModel(
#   model_name="gemini-1.5-pro",
#   generation_config=generation_config,
#   system_instruction="You're an expert in body-building, fitness, and diet-planning for the fitness professionals over 25 years. You also have a exercise therapy and a nutrition phd degree from John Hopkins University. Now, you're a full time fitness coach and nutritionists who helps over 10,000 individuals. ",
# )

# def chat():
#   print(f"Bot: How can I help you today?\n")
#   while True:
#     user_input = input("You: ")
#     if user_input != "quit":
#       chat_session = model.start_chat(history=history)
#       response = chat_session.send_message(user_input)
      
#       model_response =  response.text
#       print(f'Bot: {model_response}\n')
      
#       history.append({"role": "user", "parts": [user_input]}) # The format is dictionary
#       history.append({"role": "user", "parts": [model_response]}) # The format is dictionary
#       return 
#     else:
#       break
