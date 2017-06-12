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

number_of_buckets = 0
number_of_objects = 0

for bucket in conn.get_all_buckets():
    for key in bucket.list():
        key.delete()
        number_of_objects += 1

    conn.delete_bucket(bucket.name)
    number_of_buckets += 1

print("Total buckets deleted: " + str(number_of_buckets))
print("Total objects deleted: " + str(number_of_objects))
