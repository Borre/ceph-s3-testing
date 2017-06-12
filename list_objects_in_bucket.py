import boto
import boto.s3.connection
import config
import sys

conn = boto.connect_s3(
    aws_access_key_id = config.s3['access_key'],
    aws_secret_access_key = config.s3['secret_key'],
    host = config.s3['endpoint'],
    is_secure = config.s3['is_secure'],
    calling_format = boto.s3.connection.OrdinaryCallingFormat()
    )

if len(sys.argv) > 1 :
    bucket_name = sys.argv[1]
    try:
        bucket = conn.get_bucket(bucket_name)
        print("Objects in bucket " + bucket_name)
        for key in bucket.list():
                print "{name}\t{size}\t{modified}".format(
                        name = key.name,
                        size = key.size,
                        modified = key.last_modified,
                        )

        pass
    except Exception as e:
        print("there is no bucket \n \n \n")
        raise
else:
    print("You need to provide a bucket name")
