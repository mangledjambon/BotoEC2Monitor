__author__ = 'sean'

# TODO print out all instances and details (AMI ID, instance type, region, time of launch)

import boto.ec2

ec2 = boto.ec2.connect_to_region('us-west-2')           # connect to region where instance is located

reservations = ec2.get_all_reservations()               # get list of all reservations
assert isinstance(reservations[0].instances, object)    # assert that reservation contains ec2 instances
instances = reservations[0].instances                   # get list of ec2 instances
instance = instances[0]                                 # get the first ec2 instance


print "\nInstance id: "
print "Hostname: "
print "Instance type: \t\t" + instance.instance_type
print "Location: \t\t\t" + instance.placement
print "Time of launch: "

s3 = boto.connect_s3()






