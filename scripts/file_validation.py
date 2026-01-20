import os
import sys

REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    ".github/workflows/python-ci.yml"
]

def validate_required_files():
    missing_files = []

    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print("Missing required files:")
        for file in missing_files:
            print(f" - {file}")
        sys.exit(1)

    print("All required files are present.")

if __name__ == "__main__":
    validate_required_files()
