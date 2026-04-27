import json
import sys

file = sys.argv[1]

try:
    with open(file, 'r') as f:
        content = f.read()
    json.loads(content)
    print(f"✅ {file} is valid JSON")
    sys.exit(0)
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON in {file}")
    print(f"   Error:  {e.msg}")
    print(f"   Line:   {e.lineno}")
    print(f"   Column: {e.colno}")
    lines = content.splitlines()
    if e.lineno <= len(lines):
        bad_line = lines[e.lineno - 1]
        print(f"\n   {bad_line}")
        print(f"   {' ' * (e.colno - 1)}^")
    sys.exit(1)