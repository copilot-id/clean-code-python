# exercise code

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

try:
    content = read_file('nonexistent_file.txt')
    print(content)
except Exception as e:
    print("Error:", e)
