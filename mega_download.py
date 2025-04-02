import json
import subprocess
import sys
import os

def download_with_megadl(url, download_path):
    try:
        # Ensure the download directory exists
        os.makedirs(download_path, exist_ok=True)

        # Run megadl command with the output directory specified, capturing both stdout and stderr
        process = subprocess.Popen(
            ["megadl", "--path", download_path, url],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Redirect stderr to stdout
            text=True,
            bufsize=1  # Line buffering
        )

        # Process the combined stdout and stderr in real-time
        for line in process.stdout:
            line = line.strip()
            print(line)  # Print both stdout and stderr lines as they appear

            # Check if download limit error occurs
            if "over quota" in line.lower() or "server returned 509" in line.lower():
                print(f"Quota exceeded detected for {url}. Stopping script.")
                process.kill()  # Terminate the process
                sys.exit(1)

        process.stdout.close()
        process.wait()  # Ensure process completes

        # If the process exits successfully
        if process.returncode == 0:
            print(f"Successfully downloaded: {url} to {download_path}")
            return True
        else:
            print(f"Failed to download: {url}. Exit code: {process.returncode}")
            return False

    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")
        return False

# Function to update the JSON file after successful downloads
def update_json_file(json_file, urls_to_remove):
    try:
        with open(json_file, "r") as f:
            data = json.load(f)

        # Remove successfully downloaded URLs
        remaining_urls = [entry for entry in data["downloads"] if entry["url"] not in urls_to_remove]

        # Update the JSON file with remaining URLs
        data["downloads"] = remaining_urls
        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)
        print("Updated JSON file with remaining URLs.")
    except Exception as e:
        print(f"An error occurred while updating the JSON file: {e}")

# Main function
def main(json_file):
    try:
        # Load URLs and paths from the JSON file
        with open(json_file, "r") as f:
            data = json.load(f)

        downloads = data.get("downloads", [])
        if not downloads:
            print("No downloads found in the JSON file.")
            return
        
        
	# Download each URL one by one
        for entry in downloads:
            url = entry.get("url")
            download_path = entry.get("download_path", ".")  # Default to the current directory if no path is provided

            if url:
                print(f"Downloading {url} to {download_path}")
                if download_with_megadl(url, download_path):
                    update_json_file(json_file, [url])

    except FileNotFoundError:
        print(f"JSON file {json_file} not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide the path to your JSON file
    json_file_path = "/d/NAS/scripts/mega_download_urls.json"
    main(json_file_path)
