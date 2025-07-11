import os


def write_file(working_directory, file_path, content):
    # Ensure the working directory is an absolute path
    working_directory = os.path.abspath(working_directory)
    # If a file path is provided, join it with the working directory to get the full path
    if file_path != None:
        path = os.path.join(working_directory, file_path)
        # Ensure the full path is an absolute path
        path = os.path.abspath(path)
    # If no file path is provided, use the working directory itself
    else:
        path = working_directory
    # Check that the final path is within the permitted working directory
    if not path.startswith(working_directory):
        return f'Error: Cannot write to "{path}" as it is outside the permitted working directory'

    try:
        # Open the file in write mode
        with open(path, "w") as output_file:
            # Write the content to the file
            output_file.write(content)
            # Return a success message with the file path and number of characters written
            return f'Successfully wrote to "{path}" ({len(content)} characters written)'
    except Exception as e:
        # If an error occurs, return an error message with the exception
        return f"Error: {e}"
