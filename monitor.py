__author__ = 'sean'

# TODO connect to my instance
# TODO print out all instances and details (AMI ID, instance type, region, time of launch)

import boto
import boto.ec2

ec2 = boto.ec2.connect_to_region('us-west-2')
print(ec2)

key_name = 'EC2_pyCloud'
key_dir = '~/Downloads'

try:
    key = ec2.get_all_key_pairs(keynames=[key_name])[0]
except ec2.ResponseError,e :
    if e.code == 'InvalidKeyPair.NotFound':
        print 'Creating KeyPair: %s' % key_name

        key = ec2.create_key_pair(key_name)
        key.save(key_dir)
    else:
        raise

reservations = ec2.run_instances(
    image_id='ami-d0d8b8e0',
    key_name=key_name,
    instance_type='t1.micro',
    security_groups='ssh-access'
)







