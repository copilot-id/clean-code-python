# exercise code

def read_file(file_path: str) -> str:
    """
    Read the contents of a file and handle file-related errors.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except IOError:
        print("Error: An I/O error occurred.")
        return None

content = read_file('nonexistent_file.txt')
if content is not None:
    print(content)
