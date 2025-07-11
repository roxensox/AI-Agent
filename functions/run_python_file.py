import os, subprocess

def run_python_file(working_directory, file_path):
    # Get the absolute path of the working directory
    working_directory = os.path.abspath(working_directory)
    # If a file path is provided, construct the full path to the file
    if file_path != None:
        path = os.path.join(working_directory, file_path)
        path = os.path.abspath(path)
    # If no file path is provided, use the working directory as the path
    else:
        path = working_directory

    # Security check: Ensure the path is within the permitted working directory
    if not path.startswith(working_directory):
        return f'Error: Cannot execute "{path}" as it is outside the permitted working directory'

    # Check if the file exists
    if not os.path.exists(path):
        return f'Error: File "{path}" not found.'

    # Check if the path is a file
    if not os.path.isfile(path):
        return f'Error: "{path}" is not a file'

    # Check if the file is a Python file
    if not path.split(".")[-1] == "py":
        return f'Error: "{path}" is not a Python file.'

    # Try to run the Python file using subprocess
    try:
        out = ""
        # Execute the Python file using python3, with a timeout of 30 seconds, capturing stdout and stderr
        ret = subprocess.run(["python3", path], timeout=30, capture_output=True)
        # If there is no output, indicate that
        if ret.stdout == b'' and ret.stderr == b'':
            out += "No output produced."
            return out
        # Decode and format the output from stdout and stderr
        out += f'STDOUT: {ret.stdout.decode()}\nSTDERR: {ret.stderr.decode()}'
        # If the process exited with a non-zero code, add the return code to the output
        if ret.returncode != 0:
            out += f'\nProcess exited with code {ret.returncode}'
        return out
    # Catch any exceptions that occur during execution
    except:
        return f'Error: Unable to run "{path}"'
