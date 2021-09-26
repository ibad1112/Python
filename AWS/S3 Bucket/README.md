This python script can be used to connect to an AWS S3 bucket and read a specific file from a list of objects stored in S3. To do this we will use Python SDK for AWS more commonly known as boto3. To run this script one can use any Python IDE. The first step involves importing the necessary packages into the IDE. The Boto module provides an easy to use, object-oriented API, as well as low-level access to AWS resources. Currently the languages supported by the SDK are node.js, Java, .NET, Python, Ruby, PHP, GO, C++, JS (Browser version) and mobile versions of the SDK for Android and iOS. The code can be found here [Python-Webapp](AWS/S3 Bucket/S3_Bucket_Access_using_SDK.py)

For accessing S3 bucket in AWS account, we also need an access token key (Token ID analogous to a username) and a secret access key (analogous to a password) to access AWS resources, like EC2 and S3 via an SDK. One can also access any public bucket without any keys using

```
s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
```

Identify, the bucket that you would like to access where you have your data stored. Once you have the identified the name of the bucket for example ‘xyz’, you can assign this name to the variable named S3_BUCKET_NAME.

For accessing the objects in the bucket named “S3_BUCKET_NAME”, with the Bucket() method, assign the list of objects into a variable named your_bucket. The for loop in the below script reads the objects one by one in the bucket, named “your_bucket”, looking for objects without any prefix. Once it finds the object, the object name is printed out. To use a prefix search for the objects enter the prefix in the location 

```
for file in your_bucket.objects.filter(Prefix = ''):
```

