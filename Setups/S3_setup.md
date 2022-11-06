# What is S3

- S3 is Simple Storage Service.
- It is a global service which means it is highly available and scalable.
- You can store whatever you want on it as it's a storage platform, so anything you want to keep can be held on S3.

## What is required

On you EC2 Instance or any machine, you need:
- Python3 or above
- AWS-CLI
- pip3
- AWS access & secret key for data security

## Set up AWSCLI on ec2

- ssh into app vm
- Install python3 `sudo apt-get install python3`
- Check Python version python –version
- If the version is 2.... then run this command to force the use of version 3... `alias python=python3`
- Then check the version again and it should be 3.x
- Install pip3 `sudo apt-get install python3-pip`
- Install awscli `sudo pip3 install awscli`
- Run command: aws configure (can run this command again after filling in the details to check if they have been saved)
- Enter details: aws access key: enter here, secret key: enter here, region: eu-west-1, output: json


#### CRUD- Create, Read, Update, Delete

Commands run after: aws s3 ls lists all s3 buckets available (if configuration is successful)
- View all s3 buckets available  `aws s3 ls` 
- create a bucket `aws s3 mb s3://eng130-osman` - no underscores allowed use dash
- create a file to put in bucket `sudo nano`

#### When deleting a bucket you must delete all content before deleting a bucket - can only delete a empty bucket

- download object from s3 ` aws s3 cp s3://eng130-osman/testing-s3.txt newtest.txt`
- delete file - `aws s3 rm s3://eng130-osman/testing-s3.txt`
- remove bucket ` aws s3 rb s3://eng130-osman`

### How to automate CRUD

#### Creating a bucket
```
import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='bucket_name', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
```

#### Deleting a bucket
```
import boto3

s3 = boto3.client('s3')

s3.delete_bucket(Bucket = 'bucket_name')
```

#### Uploading a file
```
import boto3

s3 = boto3.client('s3')

s3.upload_file(
        Filename = 'file_name',
        Bucket = 'bucket_name',
        Key = 'file_name',
        )
```

#### Deleting a file
```
import boto3

s3 = boto3.resource('s3')

s3.Object('bucket_name', 'file_name').delete()

```

#### Download file
```
import boto3

s3 = boto3.client('s3')

s3.download_file(
        Filename = 'file_name',
        Bucket = 'bucket_name',
        Key = 'file_name',
        )
```

https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-delete-buckets