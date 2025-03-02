import os
from dotenv import load_dotenv
from google import genai
import google.generativeai as genai

def get_gemini_api_key():
     load_dotenv()
     api_key = os.getenv('GEMINI_API_KEY')
     if not api_key:
         raise ValueError("No Gemini API key found. Please set the GEMINI_API_KEY environment variable.")
     return api_key


genai.configure(api_key=get_gemini_api_key())
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Initialize the chat session
# The session is used to maintain the context of the conversation
# Previous chat session cannot be recalled

chat = model.start_chat(history=[]) #might need to moved

def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt) # Add error handling here.
        return response
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "Sorry, I encountered an error processing your request."



def AI_startup():
    prompt = open("optimal_prompt.txt","r")
    pre_prompt_response = get_ai_response(prompt)
    print("Pre-prompt response: ", pre_prompt_response)
    
