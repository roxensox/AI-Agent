import os


def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    if working_directory not in os.path.abspath(path):
        return f'Error: Cannot write to "{path}" as it is outside the permitted working directory'

    try:
        with open(path, "w") as output_file:
            output_file.write(content)
            return f'Successfully wrote to "{path}" ({len(content)} characters written)'
    except:
        return "Error: Failed to write output"
