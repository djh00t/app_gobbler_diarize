import os
from diarize.s3_interaction import download_from_s3, upload_to_s3

# Get AWS credentials from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")
aws_s3_bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

# Make sure the credentials are set
if aws_access_key_id is None:
    raise ValueError("AWS_ACCESS_KEY_ID environment variable is not set.")
if aws_secret_access_key is None:
    raise ValueError("AWS_SECRET_ACCESS_KEY environment variable is not set.")
if aws_default_region is None:
    raise ValueError("AWS_DEFAULT_REGION environment variable is not set.")
if aws_s3_bucket_name is None:
    raise ValueError("AWS_S3_BUCKET_NAME environment variable is not set.")

# Generate a test 1mb file
def generate_1mb_binary_file(filename):
    """Generates a 1MB binary file with random data.

    Args:
        filename: The name of the file to generate.
    """

    file_size_in_bytes = 1024 * 1024
    with open(filename, "wb") as f:
        f.write(os.urandom(file_size_in_bytes))

generate_1mb_binary_file("test_file.dat")

# Upload a file to S3, read local file into content field
upload_to_s3(aws_s3_bucket_name, "tests/test_file.dat", content=open("test_file.dat", "rb").read())

# Remove the local file
os.remove("test_file.dat")

# Download a file from S3, write content field to local file
download_from_s3(aws_s3_bucket_name, "tests/test_file.dat")