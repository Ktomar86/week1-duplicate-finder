import hashlib
from pathlib import Path

def list_files(folder_path):
    
    folder = Path(folder_path)
    
    files = []
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
    
    return files

import hashlib
from pathlib import Path

def get_file_hash(file_path):
    """Return the MD5 hash of a file's contents as a hex string."""
    hasher = hashlib.md5()
    
    with open(file_path, "rb") as f:
        content = f.read()
        hasher.update(content)
    
    return hasher.hexdigest()

if __name__ == "__main__":
    files = list_files("test_folder")
    for f in files:
        print(f.name)