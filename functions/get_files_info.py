import os, sys

def get_files_info(working_directory, directory=None):
    path = os.path.join(working_directory, directory)
    if working_directory not in os.path.abspath(path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    output = ""

    output += f"Result for {directory} directory:\n"
    for item in os.listdir(path):
        size = os.path.getsize(os.path.join(path, item))
        output += f" - {item}: {size} bytes, is_dir={os.path.isdir(os.path.join(path, item))}\n"
    return output

if __name__ == "__main__":
    print(get_files_info("calculator", "pkg"))
