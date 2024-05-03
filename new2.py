import os
import requests

# URL of your Flask app endpoint
url = 'https://0881-103-166-59-222.ngrok-free.app/upload'

# Prompt the user to input the folder name
folder_path = input('Enter the folder path: ')

# Check if the provided folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

# Iterate over files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        # Open the file and send it as multipart/form-data
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            try:
                response = requests.post(url, files=files)
                # Print the response from the server
                print(f"Uploaded {file_path}: {response.text}")
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")
                pass
