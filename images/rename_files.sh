#!/bin/bash

# Check if the directory is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Directory to rename files in
DIR="$1"

# Counter to track file number
counter=1

# Loop over all files in the directory
for file in "$DIR"/*; do
  # Only rename if it's a file (not a directory)
  if [ -f "$file" ]; then
    # Get the full path of the new filename
    new_filename="$DIR/$counter.jpg"
    
    # Rename the file
    mv "$file" "$new_filename"
    
    echo "Renamed $file to $new_filename"
    
    # Increment the counter
    counter=$((counter + 1))
  fi
done

