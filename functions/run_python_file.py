import os, subprocess

def run_python_file(working_directory, file_path):
    path = os.path.join(working_directory, file_path)

    if working_directory not in os.path.abspath(path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(path):
        return f'Error: File "{file_path}" not found.'

    if not os.path.isfile(path):
        return f'Error: "{file_path}" is not a file'

    if not file_path.split(".")[-1] == "py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        out = ""
        err = None
        ret = subprocess.run(["python3", path], timeout=30, capture_output=True)
        out += f'STDOUT: {ret.stdout}\nSTDERR: {ret.stderr}'
        if ret.returncode != 0:
            out += f'\nProcess exited with code {ret.returncode}'
        if ret.stdout == b'':
            out = "No output produced."
        return out
    except:
        return f'Error: Unable to run "{file_path}"'
