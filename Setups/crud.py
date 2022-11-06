import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys



def create_bucket(bucket_name, region='eu-west-1'):



   try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name



   # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True



def download_file(bucket_name, object_name, file_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)



def delete_bucket(bucket_name, region="eu-west-1"):
    s3 = boto3.resource('s3', region_name=region)
    s3.Bucket(bucket_name).delete()



def delete_file(bucket, object, region="eu-west-1"):
    s3 = boto3.client('s3', region_name=region)
    s3.delete_object(Bucket=bucket, Key=object)   



# create_bucket('eng130-subhaan', 'eu-west-1')



if __name__ == "__main__":



   args = sys.argv



   globals()[args[1]](*args[2:])