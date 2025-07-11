import os, sys

def get_files_info(working_directory, directory=None):
    """Lists files in the specified directory along with their sizes, constrained to the working directory.

    Args:
        working_directory: The base working directory.
        directory: The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.
    """
    # Determine the absolute path. If directory is None, use working_directory. Otherwise, join working_directory and directory.
    path = os.path.abspath(os.path.join(working_directory, directory)) if directory != None else os.path.abspath(working_directory)
    # Security check: ensure the path is within the permitted working directory.
    if not (path.startswith(os.path.abspath(working_directory))):
        return f'Error: Cannot list "{path}" as it is outside the permitted working directory'

    # Check if the path is a directory.
    if not os.path.isdir(path):
        return f'Error: "{path}" is not a directory'

    output = ""

    output += f"Result for {path} directory:\n"
    try:
        # Iterate through the items in the directory.
        for item in os.listdir(path):
            # Get the size of the item.
            size = os.path.getsize(os.path.join(path, item))
            # Append the item's name and size to the output string.
            output += f" - {item}: {size} bytes, is_dir={os.path.isdir(os.path.join(path, item))}\n"
        return output
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_files_info("calculator", "pkg"))
