import boto3

session = boto3.session.Session()
# bucket name : test-s3
# accesskey : testuser
# secretkey : TbriQlpXm4ghPLKslhS6nkKr6+pVrB2y6+Tta3UM
# SrAvilaSeason1_2013_MX_001.mp4


s3_client = session.client(
    service_name='s3',
    aws_access_key_id='testuser',
    aws_secret_access_key='TbriQlpXm4ghPLKslhS6nkKr6+pVrB2y6+Tta3UM',
    endpoint_url='http://172.27.63.160:9020',
    use_ssl=False,
)

print(s3_client.list_buckets())
