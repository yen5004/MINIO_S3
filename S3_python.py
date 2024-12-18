# Use this script to test S3 API via python

import boto3
from botocore.exceptions import NoCredentialsError

# Set up MinIO client
s3 = boto3.client(
    's3',
    endpoint_url='http://10.10.84.212:9000',  # MinIO server URL
    aws_access_key_id='XXXX',
    aws_secret_access_key='XXXXXXXX',
    region_name='us-east-1' # MinIO doesnt require this bt its commonly used fo>
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False # Set to True if yo have valid SSL certificates
)

try:
    # List buckets
    response = s3.list_buckets()
    print("Buckets:", response['Buckets'])
except NoCredentialsError:
    print("Credentials not available")
