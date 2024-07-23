"""
qq - A command-line interface for querying AI using OpenAI's API.
This module provides functionality to interact with an AI assistant
for various queries related to Linux, terminal usage, and programming.
"""

import os
import sys
import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    """
    Get AI response for the given prompt using OpenAI's API.

    Args:
    prompt (str): The user's query.

    Returns:
    str: The AI's response to the query.
    """
    try:
        messages = [
            {"role": "system", "content": (
                "You are a Linux-based assistant, expert at terminal, bash, and programming. "
                "Your answers should be factual and concise while adding the required information to the user. "
                "Use markdown formatting in your responses to enhance readability."
            )},
            {"role": "user", "content": f"Query: {prompt}\nResponse:"}
        ]
        ai_response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1500
        )
        return ai_response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"An error occurred with the OpenAI API: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def main():
    """Main function to handle command-line interface."""
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
        response = get_ai_response(user_query)
        console = Console()
        md = Markdown(response)
        console.print("\nqq:", style="bold")
        console.print(md)
    else:
        print("Usage: qq <your question>")

if __name__ == "__main__":
    main()