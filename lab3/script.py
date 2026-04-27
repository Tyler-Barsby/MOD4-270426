import sys
import datetime

# Read the uploaded file passed as argument
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    contents = f.read()

# Do some processing
results = []
results.append(f"Processed: {datetime.datetime.now()}")
results.append(f"Line count: {len(contents.splitlines())}")
results.append(f"Word count: {len(contents.split())}")
results.append(f"Uppercase output:")
results.append(contents.upper())

with open(output_file, 'w') as f:
    f.write("\n".join(results))

print("Script completed successfully")