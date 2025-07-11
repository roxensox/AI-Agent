import config as cfg, os


def get_file_content(working_directory, file_path):
    """Read file contents within the specified working directory."""
    # Convert the working directory to an absolute path for security.
    working_directory = os.path.abspath(working_directory)

    # If a file path is provided, construct the full path.
    if file_path != None:
        path = os.path.join(working_directory, file_path)
        # Ensure the constructed path is an absolute path.
        path = os.path.abspath(path)
    # If no file path is provided, default to the working directory itself.
    else:
        path = working_directory

    # Security check: Ensure the requested path is within the allowed working directory.
    if not path.startswith(working_directory):
        return f'Error: Cannot read "{path}" as it is outside the permitted working directory'

    # Check if the file exists.
    if not os.path.isfile(path):
        return f'Error: "{path}" is not a file'

    # Attempt to read the file content.
    try:
        with open(path, "r") as inFile:
            # Read up to the maximum allowed characters from the file.
            output = inFile.read(cfg.MAX_CHARS)
            # Check if there's more content beyond the limit, and truncate if necessary.
            if inFile.read(1) != "":
                output += f"[...File '{path}' truncated at 10000 characters]"
            return output
    except Exception as e:
        # Handle potential exceptions during file reading.
        return f"Error: {e}"


if __name__ == "__main__":
    # Example usage: Read the content of this same file.
    print(get_file_content(".", "get_file_content.py"))
