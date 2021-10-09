from typing import List


def write_files(files: List[List[str]]):
    for file_content in files:
        file_name, content = file_content
        with open(file_name, "w") as file:
            file.write(content)
