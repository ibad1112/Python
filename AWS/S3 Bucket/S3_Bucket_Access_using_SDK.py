import boto3
import botocore

from botocore import UNSIGNED
from botocore.config import Config

S3_BUCKET_NAME = 'PUT YOUR BUCKET NAME HERE' # Enter the bucket name you want to access 

# Either use this one if you want to access a public bucket without any KEYS

s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))

# Or Use this one if you have the Keys to the aws account which hosts the bucket

s3 = boto3.resource('s3',
                    aws_access_key_id= 'YOUR_ACCESS_KEY_ID',
                    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY')


your_bucket=s3.Bucket(S3_BUCKET_NAME)

for file in your_bucket.objects.filter(Prefix = ''): # Prefix can be added here as well if you want to find a file with a specific prefix
    file_name=file.key
    print(file_name)