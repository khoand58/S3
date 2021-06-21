import boto3
import pprint
session = boto3.session.Session()
# bucket name : test-s3
# accesskey : testuser
# secretkey : TbriQlpXm4ghPLKslhS6nkKr6+pVrB2y6+Tta3UM
# SrAvilaSeason1_2013_MX_001.mp4


s3_client = session.client(
    service_name='s3',
    aws_access_key_id='root',
    aws_secret_access_key='ClpygUZVXMNYnqY0aTcd1b3txnFwWW/lITERNeRf',
    endpoint_url='http://172.27.64.165:9020',
    use_ssl=False,
)

pprint.pprint(s3_client.list_buckets())
