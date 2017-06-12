import boto
import boto.s3.connection
import config

conn = boto.connect_s3(
    aws_access_key_id = config.s3['access_key'],
    aws_secret_access_key = config.s3['secret_key'],
    host = config.s3['endpoint'],
    is_secure = config.s3['is_secure'],
    calling_format = boto.s3.connection.OrdinaryCallingFormat()
    )

print('Listing buckets: \t')
for bucket in conn.get_all_buckets():
    print(bucket.name + " \t" + bucket.creation_date)
