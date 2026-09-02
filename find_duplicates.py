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


def find_duplicate_groups(files):
    """Group files by content hash. Returns a dict of {hash: [list of duplicate files]}."""
    hash_map = {}

    for file_path in files:
        file_hash = get_file_hash(file_path)

        if file_hash not in hash_map:
            hash_map[file_hash] = []

        hash_map[file_hash].append(file_path)

    duplicates = {}
    for file_hash, file_list in hash_map.items():
        if len(file_list) > 1:
            duplicates[file_hash] = file_list

    return duplicates


if __name__ == "__main__":
    files = list_files("test_folder")
    duplicates = find_duplicate_groups(files)

    for file_hash, file_list in duplicates.items():
        print(f"Duplicate group (hash: {file_hash}):")
        for f in file_list:
            print(f"  - {f.name}")