import boto3
from boto3.s3.transfer import TransferConfig
import os
import threading
import sys

# default
# bucket_name = 'test-s3'
# aws_access_key_id='root',
# aws_secret_access_key='ClpygUZVXMNYnqY0aTcd1b3txnFwWW/lITERNeRf',
# endpoint_url='http://172.27.64.165:9020',
# use_ssl=False
# aws_access_key_id = 'root'
# aws_secret_access_key = 'ClpygUZVXMNYnqY0aTcd1b3txnFwWW/lITERNeRf'
# endpoint_url = 'http://172.27.64.165:9020'
# use_ssl = False

bucket_name = 'test-s3'
# bucket name : test-s3
# accesskey : testuser
# secretkey : TbriQlpXm4ghPLKslhS6nkKr6+pVrB2y6+Tta3UM
# SrAvilaSeason1_2013_MX_001.mp4
aws_access_key_id = 'testuser'
aws_secret_access_key = 'TbriQlpXm4ghPLKslhS6nkKr6+pVrB2y6+Tta3UM'
endpoint_url = 'http://172.20.2.90:9020'
use_ssl = False
s3_resource = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                             endpoint_url=endpoint_url, use_ssl=False, )

# multipart_threshold : Ensure that multipart uploads/downloads only happen if the size of a transfer
# is larger than 25 MB
# multipart_chunksize : Each part size is of 25 MB
config = TransferConfig(multipart_threshold=1024 * 25,
                        max_concurrency=10,
                        multipart_chunksize=1024 * 25,
                        use_threads=True)


# Function to upload the file to s3 using multipart functionality
def multipart_upload_boto3():
    file_path = os.path.dirname(__file__) + '/test.pdf'
    key = 'vod/test.pdf'

    s3_resource.Object(bucket_name, key).upload_file(file_path,
                                                     ExtraArgs={'ContentType': 'text/pdf'},
                                                     Config=config,
                                                     Callback=ProgressPercentage(file_path)
                                                     )


# Function to download the file to s3 using multipart functionality
def multipart_download_boto3(name_file, key_file):
    file_path = os.path.dirname(__file__) + name_file
    print(os.path.dirname(__file__))
    file_path1 = os.path.dirname(__file__)
    # file_path1 = 'C:\\Users\\FPT\\OneDrive\\Desktop\\'
    key = key_file

    s3_resource.Object(bucket_name, key).download_file(file_path,
                                                       Config=config,
                                                       Callback=ProgressPercentage(file_path1)
                                                       )


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


if __name__ == '__main__':
    # multipart_upload_boto3()
    multipart_download_boto3('/VOD/ADSL/VOD/01_Test/', 'VOD/ADSL/VOD/01_Test/KnightsAndMagic_2017_JP_ok.mp4')
