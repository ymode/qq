"""
qq - A command-line interface for querying AI using llama-3.
This module provides functionality to interact with an AI assistant
for various queries related to Linux, terminal usage, and programming.
"""
import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from halo import Halo
from huggingface_hub import InferenceClient

load_dotenv()

def get_ai_response(prompt):
    """
    Get AI response for the given prompt using llama-3.
    Args:
    prompt (str): The user's query.
    Returns:
    str: The AI's response to the query.
    """
    try:
        client = InferenceClient(
            "meta-llama/Meta-Llama-3.1-8B-Instruct",
            token=os.getenv("HUGGINGFACE_TOKEN")
        )
        
        messages = [
            {"role": "system", "content": (
                "You are a Linux-based assistant, expert at terminal, bash, and programming."
                "Your answers should be factual and concise." 
                "while adding the required information to the user."
                "Use markdown formatting in your responses to enhance readability."
            )},
            {"role": "user", "content": f"Query: {prompt}\nResponse:"}
        ]
        
        response = ""
        for message in client.chat_completion(
            messages=messages,
            max_tokens=1500,
            stream=True,
        ):
            response += message.choices[0].delta.content or ""
        
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """Main function to handle command-line interface."""
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
        # Create and start the spinner
        spinner = Halo(text='Thinking...', spinner='dots')
        spinner.start()
        try:
            response = get_ai_response(user_query)
            # Stop the spinner before printing the response
            spinner.stop()
            console = Console()
            md = Markdown(response)
            console.print("\nqq:", style="bold")
            console.print(md)
        except Exception as e:
            spinner.fail(f"An error occurred: {str(e)}")
    else:
        print("Usage: qq <your question>")

if __name__ == "__main__":
    main()