import os
from firebase_admin import credentials, storage, initialize_app

# Path to your service account JSON file
service_account_path = 'path/to/serviceAccountKey.json'

# Initialize Firebase using the service account credentials
cred = credentials.Certificate(service_account_path)
initialize_app(cred)

bucket_name = '<your-firebase-storage-bucket>'
folder_path = 'path/to/photos/folder/'

def download_photos_from_firebase(bucket_name, folder_path, local_folder_path):
    bucket = storage.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_path)

    for blob in blobs:
        # Extract the filename from the blob path
        filename = os.path.basename(blob.name)

        # Download the photo to the local folder
        blob.download_to_filename(os.path.join(local_folder_path, filename))
        print(f'Downloaded: {filename}')

# Local folder path on your Raspberry Pi to save the downloaded photos
local_folder_path = '/path/to/local/folder'

# Create the local folder if it doesn't exist
if not os.path.exists(local_folder_path):
    os.makedirs(local_folder_path)

# Download the photos from Firebase Storage
download_photos_from_firebase(bucket_name, folder_path, local_folder_path)
