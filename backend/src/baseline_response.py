import openai
import os
from dotenv import load_dotenv

# Load environment variables. 
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def get_baseline_response(prompt: str) -> str:
    """
    Gets a baseline response from OpenAI API for the given prompt.
    
    Args:
        prompt (str): The input prompt/question
        
    Returns:
        str: The AI's response
    """
    client = openai.OpenAI(api_key=openai.api_key)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=1000
    )
    
    return response.choices[0].message.content

print(get_baseline_response("How to turn off my iPhone?"))