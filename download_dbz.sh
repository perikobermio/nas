#!/bin/bash

# Base URL
base_url="https://downloads.zital.eus/db/02-dbz/"

# Destination directory
dest_dir="/d/NAS/Serijek/Dragoi bola Z"

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Loop through the numbers 001 to 291
for i in $(seq -f "%03g" 1 291)
do
    # Construct the full URL
    file_url="${base_url}${i}.mp4"
    
    # Construct the full path for the destination file
    dest_file="${dest_dir}/${i}.mp4"
    
    # Download the file
    echo "Downloading ${file_url} to ${dest_file}..."
    curl -o "${dest_file}" "${file_url}"
    
    # Check if the download was successful
    if [ $? -ne 0 ]; then
        echo "Failed to download ${file_url}"
    else
        echo "Downloaded ${file_url} successfully"
    fi
done

