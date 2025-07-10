import os
import sys
import re
import config as cfg
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def get_prompt() -> str:
    '''
    Gets the prompt from the command line and exits if none was provided.
    '''
    # If an extra argument was provided, returns it as a string for the prompt
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        # Prints an error message an exits with error code 1
        print("Error: Please enter a prompt.")
        sys.exit(1)


def main():
    '''
    Sends user interaction to gemini 2.0 flash and prints the response
    '''
    # gets the user prompt
    prompt = get_prompt()

    # Adds the prompt to the context
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    # Makes the request
    response = client.models.generate_content(
        model=cfg.MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=cfg.SYSTEM_PROMPT),
    )

    # Prints the response text
    print(response.text)

    # Initializes verbose setting as false
    verbose = False

    # Avoids index out of range error while checking if the verbose tag was provided
    try:
        verbose = sys.argv[2] == "--verbose"
    except:
        pass

    # If the user provided the tag, prints extra details
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # Standard exit code
    sys.exit(0)


if __name__ == "__main__":
    main()
