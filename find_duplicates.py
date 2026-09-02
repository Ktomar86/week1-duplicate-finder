import argparse
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

def delete_duplicates(duplicates, dry_run=True):
    """Delete duplicate files, keeping the first file in each group. Returns count of files deleted (or that would be deleted, in dry-run)."""
    deleted_count = 0

    for file_hash, file_list in duplicates.items():
        keep_file = file_list[0]
        files_to_delete = file_list[1:]

        print(f"Keeping: {keep_file.name}")

        for file_path in files_to_delete:
            if dry_run:
                print(f"  [DRY RUN] Would delete: {file_path.name}")
                deleted_count += 1
            else:
                try:
                    file_path.unlink()
                    print(f"  Deleted: {file_path.name}")
                    deleted_count += 1
                except Exception as error:
                    print(f"  Could not delete {file_path.name}: {error}")

    return deleted_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find duplicate files in a folder based on content, not filename.")
    parser.add_argument("--folder", required=True, help="Path to the folder to scan for duplicates")
    parser.add_argument("--delete-duplicates", action="store_true", help="Delete duplicate files, keeping one copy of each")
    parser.add_argument("--dry-run", action="store_true", help="Preview deletions without actually deleting anything")

    args = parser.parse_args()

    files = list_files(args.folder)
    duplicates = find_duplicate_groups(files)

    if not duplicates:
        print("No duplicates found.")
    else:
        for file_hash, file_list in duplicates.items():
            print(f"Duplicate group (hash: {file_hash}):")
            for f in file_list:
                print(f"  - {f.name}")

        if args.delete_duplicates:
            print("\n--- Deletion ---")
            count = delete_duplicates(duplicates, dry_run=args.dry_run)
            if args.dry_run:
                print(f"\n[DRY RUN] Would have deleted {count} file(s).")
            else:
                print(f"\nDeleted {count} file(s).")