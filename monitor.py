__author__ = 'sean'

import boto.ec2

ec2 = boto.ec2.connect_to_region('us-west-2')

print(ec2.aws_access_key_id)






