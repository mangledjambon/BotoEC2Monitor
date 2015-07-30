__author__ = 'sean'

# TODO connect to my instance
# TODO print out all instances and details (AMI ID, instance type, region, time of launch)

import boto.ec2

ec2 = boto.ec2.connect_to_region('us-west-2')
print(ec2)






