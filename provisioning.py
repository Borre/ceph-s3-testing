import boto
import boto.s3.connection
import config

number_of_objects_per_bucket = int(round(config.s3['number_of_objects']/config.s3['number_of_buckets']))

conn = boto.connect_s3(
    aws_access_key_id = config.s3['access_key'],
    aws_secret_access_key = config.s3['secret_key'],
    host = config.s3['endpoint'],
    is_secure = config.s3['is_secure'],
    calling_format = boto.s3.connection.OrdinaryCallingFormat()
    )

for i in range(0, config.s3['number_of_buckets']):
    try:
        bucket_number = str('{:0>5}'.format(i))
        bucket_name = 'c' + bucket_number
        bucket = conn.create_bucket(bucket_name)
        print("Creating bucket: " + bucket_name)

        print("Creating " + str(number_of_objects_per_bucket) + " objects in " + bucket_name + " bucket")

        for key_object in range(0, number_of_objects_per_bucket):
            try:
                object_name = bucket_name + "-" + str(key_object) + ".txt"
                key_creation = bucket.new_key(object_name)
                key_creation.set_contents_from_string(object_name)
                print("Object: " + object_name + " created!")
                pass
            except Exception as error:
                print(error)
                raise

    except Exception as exe:
        print(exe)
        raise
