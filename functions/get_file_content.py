import config as cfg, os

def get_file_content(working_dir, file_path):
    path = os.path.join(working_dir, file_path)
    if working_dir not in os.path.abspath(path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(path):
        return f'Error: "{file_path}" is not a file'

    try:
        with open(path, "r") as inFile:
            output = inFile.read(cfg.MAX_CHARS)
            if inFile.read(1) != "":
                output += f"[...File '{file_path}' truncated at 10000 characters]"
            return output
    except:
        return "Error: could not read file."


if __name__ == "__main__":
    print(get_file_content(".", "get_file_content.py"))
