__author__ = 'sean'

# TODO print out all instances and details (AMI ID, instance type, region, time of launch)
# TODO fix bucket permissions!!

import boto.ec2

ec2 = boto.connect_ec2()           # connect to region where instance is located
regions = ec2.get_all_regions()

for r in regions:
    connection = boto.connect_ec2(region=r)
    print r.name
    reservations = connection.get_all_instances()               # get list of all reservations
    instances = [index for reservation in reservations for index in reservation.instances]

    if instances.__len__() < 1:
        print "No instances in this region"
        print "==================================="
    else:
        for instance in instances:
            print "ID: \t\t\t" + instance.id
            print "Instance Type:\t\t" + instance.instance_type
            print "Launch Time: \t\t" + instance.launch_time
            print "==================================="

s3 = boto.connect_s3()

buckets = s3.get_all_buckets()

for bucket in buckets:
    print bucket.name








