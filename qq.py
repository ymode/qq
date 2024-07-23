import os
import sys
import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    try:
        messages = [
            {"role": "system", "content": "You are a Linux-based assistant, expert at terminal, bash, and programming. Your answers should be factual and concise while adding the required information to the user. Use markdown formatting in your responses to enhance readability."},
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
        response = get_ai_response(query)
        console = Console()
        md = Markdown(response)
        console.print("\nqq:", style="bold")
        console.print(md)
    else:
        print("Usage: qq <your question>")