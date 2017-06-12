# ceph-s3-testing
Tools for test S3 API in ceph

# Setup
```
pip install requirements.txt
```
Now you can configure the parameters of your ceph in config.py, you need:

 - IP of the endpoint of Rados Gateway
 - S3 account access key
 - S3 account secret key
 - Setup if the endpoint have SSL (default false)
 - Configure the number of objects and buckets for the tests

# Scripts

**provisioning.py**

This script create the buckets and the objects in the storage.

Usage:
```
python provisioning.py
```
**list_buckets.py**

List the buckets in the account.

Usage:
```
python list_buckets.py
```

**list_objects_in_bucket.py**

List the objects created in a desired bucket.

Usage:
```
python provisioning.py name_of_the_bucket
```

**deleting.py**

Delete all the buckets and objects in the account.

Usage:
```
python provisioning.py
```

Any bug, please raise a issue or contact me at ehernandez@suse.com
