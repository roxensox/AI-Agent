from google.genai import types

MAX_CHARS = 10000
MODEL_NAME = "gemini-2.0-flash-001"
MAX_ITERS = 20

SCHEMA_GET_FILES_INFO = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
SCHEMA_GET_FILE_CONTENT = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the contents of.",
            ),
        },
    ),
)
SCHEMA_WRITE_FILE = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)
SCHEMA_RUN_PYTHON_FILE = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to run",
            ),
        },
    ),
)

AVAILABLE_FUNCTIONS = types.Tool(
    function_declarations=[
        SCHEMA_GET_FILES_INFO,
        SCHEMA_GET_FILE_CONTENT,
        SCHEMA_WRITE_FILE,
        SCHEMA_RUN_PYTHON_FILE,
    ]
)

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
