import boto3
from src.config import settings

class ObjectStorage:
    def __init__(self, region: str, bucket: str):
        self.bucket = bucket
        self.client = boto3.client(
            "s3",
            region_name=settings.R2_REGION,
            endpoint_url=settings.R2_ENDPOINT,
            aws_access_key_id=settings.R2_ACCESS_KEY,
            aws_secret_access_key=settings.R2_SECRET_KEY,
        )

    def download(self, object_key: str, local_path: str):
        self.client.download_file(self.bucket, object_key, local_path)
