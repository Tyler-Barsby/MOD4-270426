import sys
import subprocess
import json

input_file = sys.argv[1]

# Try to detect if it's JSON
def is_json(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, UnicodeDecodeError):
        return False

# Try to detect if it's plain text
def is_text(filepath):
    try:
        with open(filepath, 'r') as f:
            f.read()
        return True
    except UnicodeDecodeError:
        return False

if is_json(input_file):
    print("🔍 Detected: JSON file — running lint.py")
    result = subprocess.run(
        ['python3', 'lab3/lint.py', input_file],
        capture_output=False
    )
    sys.exit(result.returncode)

elif is_text(input_file):
    print("📄 Detected: Text file — running script.py")
    result = subprocess.run(
        ['python3', 'lab3/script.py', input_file, 'processed_file.txt'],
        capture_output=False
    )
    sys.exit(result.returncode)

else:
    print("❌ Unknown file type — cannot process")
    sys.exit(1)