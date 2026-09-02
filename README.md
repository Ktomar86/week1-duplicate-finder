# Duplicate File Finder

A command-line tool that finds duplicate files in a folder by comparing file **content**, not filenames — with an optional safe cleanup mode.

## Features
- Detects duplicate files using MD5 content hashing, so renamed copies are still caught
- Groups duplicates together and shows which files match
- Optional `--delete-duplicates` mode that keeps one copy of each file and removes the rest
- `--dry-run` flag to preview exactly what would be deleted before anything actually happens

## Requirements
- Python 3.11+ (no external packages needed — uses only the standard library)

## Installation
1. Clone this repository:
```bash
   git clone https://github.com/Ktomar86/week1-duplicate-finder.git
   cd week1-duplicate-finder
```
2. (Optional but recommended) Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\Activate.ps1   # Windows
   source venv/bin/activate    # Mac/Linux
```

## Usage

Find duplicates (report only, no changes):
```bash
python find_duplicates.py --folder ./test_folder
```

Preview what would be deleted, without deleting anything:
```bash
python find_duplicates.py --folder ./test_folder --delete-duplicates --dry-run
```

Actually delete duplicates (keeps the first file found in each group):
```bash
python find_duplicates.py --folder ./test_folder --delete-duplicates
```

### Arguments
| Flag | Required | Description |
|---|---|---|
| `--folder` | Yes | Path to the folder to scan for duplicates |
| `--delete-duplicates` | No | Delete duplicate files, keeping one copy of each |
| `--dry-run` | No | Preview deletions without actually deleting anything |

## Example output