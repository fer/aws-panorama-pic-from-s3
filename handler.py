import boto3
import os
import json


def __download_files(bucket_name: str, files: dict):
    s3 = boto3.resource('s3')

    for file in files:
        print('Downloading ' + file)
        s3.Bucket(bucket_name).download_file(file, file)


def __stitch_images(files: dict):
    cmd = './image-stitching ' + ' '.join(filename for filename in files)
    os.system(cmd)


def stitch_s3_files(event, context):
    __download_files(event['bucket_name'], event['files'])
    __stitch_images(event['files'])


if __name__ == '__main__':
    TEST_DATA = json.loads(os.environ.get('TEST_DATA'))

    __download_files(TEST_DATA['bucket_name'], TEST_DATA['files'])
    __stitch_images(TEST_DATA['files'])
