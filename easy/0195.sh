# Read from the file file.txt and output the tenth line to stdout.

#!/bin/bash

# Specify the filename directly in the script
filename="file.txt"

# Check if the file exists
if [ ! -f "$filename" ]; then
  exit 0  # Exit silently if the file does not exist
fi

# Use sed to print the 10th line
sed -n '10p' "$filename"
