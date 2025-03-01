import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Initialize the chat session
# The session is used to maintain the context of the conversation
# Previous chat session cannot be recalled

chat = model.start_chat(history=[])  

def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt) # Add error handling here.
        return response.text
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "Sorry, I encountered an error processing your request."


def main():
    prompt = "-- You are a healthcare bot\n --When responding to the user only reply with only one medical care specalist taxomomy based on there smpytoms\n --Respond with only from this list of health care taxonomy that match the symptoms of the sure:Cardiology,Oncology,Neurology,Orthopedics,Pediatrics,Obstetrics, Gynecology,Psychiatry,Dermatology,Endocrinology,Gastroenterology,Nephrology,Pulmonology,Infectious Disease,Geriatrics,Rheumatology,Urology,Emergency Medicine,Pathology,Physical Medicine,Rehabilitation "
    pre_prompt_response = get_ai_response(prompt)
    print("Pre-prompt response: ", pre_prompt_response)
    
    print("Welcome! Let's start a conversation. Type 'exit' to end.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = get_ai_response(user_input)
        print("AI: ", ai_response)


if __name__ == "__main__":
    main()




