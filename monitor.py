__author__ = 'sean'

import boto.ec2

ec2 = boto.connect_ec2()                            # connect to EC2, returns connection object
regions = ec2.get_all_regions()                     # get list of all available regions

for r in regions:                                   # loop through all regions in list
    connection = boto.connect_ec2(region=r)         # make a connection to the region
    print r.name
    reservations = connection.get_all_instances()   # get list of all reservations

    # loop through all reservations and for each reservation, return a list of instances
    instances = [index for reservation in reservations for index in reservation.instances]

    if instances.__len__() < 1:                     # check if theres less than one instance in the region
        print "No instances running in this region"
        print "==================================="
    else:                                           # else, there must be at least one so
        for instance in instances:                  # loop through all instances, print details
            print "ID: \t\t\t" + instance.id
            print "Instance Type:\t\t" + instance.instance_type
            print "Launch Time: \t\t" + instance.launch_time
            print "==================================="

print "\nConnecting to Amazon S3...\n"
s3 = boto.connect_s3()                              # connect to S3 storage system

print "Retreiving bucket information...\n"
buckets = s3.get_all_buckets()                      # get list of all buckets for this user

for bucket in buckets:                              # loop through all buckets
    print "Bucket name: "
    print bucket.name                               # print bucket name








