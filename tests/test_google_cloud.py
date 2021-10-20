# Generic imports
import filecmp

# Local modules
from fixtures import setup_test_gcp_bucket

def test_bucket_upload(setup_test_gcp_bucket):
    source_file_name = "tests/test_google_cloud.py"
    destination_blob_name = "test_google_cloud.py"
    bucket = setup_test_gcp_bucket
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def test_bucket_download(setup_test_gcp_bucket):
    source_blob_name = "default_download_bucket_payload.txt"
    destination_file_name = "tests/default_download_bucket_payload.txt"
    reference_file_name = "data/testing/default_download_bucket_payload.txt"
    bucket = setup_test_gcp_bucket
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    filecmp.cmp(destination_file_name, reference_file_name)

            
