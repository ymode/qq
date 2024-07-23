import os
import sys
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    try:
        messages = [
            {"role": "system", "content": "You are a Linux-based assistant, expert at terminal, bash, and programming. Your answers should be factual and concise while adding the required information to the user. DO NOT USE MARKDOWN in any of your responses as your responses are streamed to the user's terminal."},
            {"role": "user", "content": f"Query: {prompt}\nResponse:"}
        ]
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"\n qq: {get_ai_response(query)}")
    else:
        print("Usage: qq <your question>")