from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
import config as cfg
from google.genai import types

def call_function(function_call_part, verbose=False):
    # Call the appropriate function based on the function_call_part
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    # Add the working directory to the arguments
    function_call_part.args["working_directory"] = "./calculator/"
    res = None


    # Call the appropriate function
    if function_call_part.name == "get_file_content":
        # Call the get_file_content function
        res = get_file_content(**function_call_part.args)
    elif function_call_part.name == "get_files_info":
        # Call the get_files_info function
        res = get_files_info(**function_call_part.args)
    elif function_call_part.name == "write_file":
        # Call the write_file function
        res = write_file(**function_call_part.args)
    elif function_call_part.name == "run_python_file":
        # Call the run_python_file function
        res = run_python_file(**function_call_part.args)
    else:
        # If the function is not found, return an error
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    # Return the result of the function call
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": res},
        )
    ],
)
