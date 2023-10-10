from klingon_file_manager import manage_file

def download_from_s3(bucket_name, file_key):
    """Download a file from an S3 bucket using the 'get' action and an s3 path.

    Args:
    bucket_name: The name of the S3 bucket.
    file_key: The key of the file to download.
    """
    manage_file(action='get', path='s3://'+bucket_name+'/'+file_key)

def upload_to_s3(bucket_name, file_key, content):
    """Upload a file to an S3 bucket using the 'post' action and an s3 path.

    Args:
    bucket_name: The name of the S3 bucket.
    file_key: The key of the file to upload.
    content: The content to upload.
    """
    manage_file(action='post', path='s3://'+bucket_name+'/'+file_key, content=content)