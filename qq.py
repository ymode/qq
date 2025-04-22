"""
qq - A beautiful markdown‑rich CLI interface for querying OpenAI or HuggingFace LLMs.

Usage examples
--------------
$ qq how do i list files by size in bash?
$ qq --model llama how do i exit vim?

Environment variables
---------------------
OPENAI_API_KEY      Required when using an OpenAI model (defaults to gpt-4o-mini).
HUGGINGFACE_TOKEN   Required when using the llama model.
"""

import os
import sys
import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from halo import Halo
import argparse
from typing import List
from rich.panel import Panel

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
LLAMA_MODEL_REPO = "meta-llama/Meta-Llama-3.1-8B-Instruct"

def _build_messages(prompt: str) -> List[dict]:
    """Construct the system & user messages for the chat completion request."""
    system_msg = (
        "You are a Linux‑based assistant, expert at the   terminal, bash and programming. "
        "Provide factual and concise answers formatted in markdown for great readability."
    )
    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt},
    ]

# ------------------------- OpenAI backend -------------------------

def _openai_response(prompt: str, model: str) -> str:
    """Query an OpenAI chat model and return the full response as a string."""
    if not openai.api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set – export it (e.g. export OPENAI_API_KEY=sk-...)"
        )

    messages = _build_messages(prompt)
    resp = openai.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1500,
    )
    return resp.choices[0].message.content

# ------------------------- Llama / HuggingFace backend -------------------------

def _llama_response(prompt: str) -> str:
    """Query the llama model on HuggingFace and return the response as a string."""
    from huggingface_hub import InferenceClient  # local import to avoid heavy dep if unused

    token = os.getenv("HUGGINGFACE_TOKEN")
    if not token:
        raise RuntimeError(
            "HUGGINGFACE_TOKEN is not set – export it (e.g. export HUGGINGFACE_TOKEN=hf_...)"
        )

    client = InferenceClient(LLAMA_MODEL_REPO, token=token)
    messages = _build_messages(prompt)

    response = ""
    for chunk in client.chat_completion(messages=messages, max_tokens=1500, stream=True):
        response += chunk.choices[0].delta.content or ""
    return response

# ------------------------- CLI -------------------------

def parse_args() -> argparse.Namespace:
    """Parse command‑line arguments."""
    parser = argparse.ArgumentParser(
        prog="qq",
        description="Ask quick questions to an AI from your terminal with beautiful markdown output.",
    )
    parser.add_argument(
        "question",
        nargs=argparse.REMAINDER,
        help="Your question for the AI. Provide anything after the options.",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="openai",
        choices=["openai", "llama"],
        help="Which provider/model to use: 'openai' (default, uses gpt-4o-mini) or 'llama' (Meta Llama‑3.1 8B)",
    )
    parser.add_argument(
        "--no-spinner",
        action="store_true",
        help="Disable the animated spinner (useful for scripts/CRON)",
    )
    return parser.parse_args()

# ------------------------- Entry point -------------------------

def main() -> None:  # type: ignore[override]
    args = parse_args()

    if not args.question:
        print("Usage: qq [--model openai|llama] <your question>")
        sys.exit(1)

    user_query = " ".join(args.question)

    spinner = None
    if not args.no_spinner:
        spinner = Halo(text="Thinking...", spinner="dots")
        spinner.start()

    try:
        if args.model == "llama":
            answer = _llama_response(user_query)
        else:
            answer = _openai_response(user_query, DEFAULT_OPENAI_MODEL)

        if spinner:
            spinner.stop()
        console = Console()
        console.print(Panel.fit("[bold cyan]Quick Question[/bold cyan]", border_style="cyan"))
        console.print("\n[bold magenta]qq:[/bold magenta]")
        console.print(Markdown(answer))
    except Exception as exc:  # pylint: disable=broad-except
        if spinner:
            spinner.fail(str(exc))
        else:
            sys.stderr.write(str(exc) + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
