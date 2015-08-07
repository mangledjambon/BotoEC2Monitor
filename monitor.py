__author__ = 'sean'

import boto.ec2

# my credentials (access key / public key) are in a boto config file in my home directory
# called ~/.boto

ec2 = boto.connect_ec2()
regions = ec2.get_all_regions()

for r in regions:
    connection = boto.connect_ec2(region=r)
    print r.name
    reservations = connection.get_all_instances()

    instances = [index for reservation in reservations for index in reservation.instances]

    if instances.__len__() < 1:
        print "No instances running in this region"
        print "==================================="
    else:
        for instance in instances:
            print "ID: \t\t\t" + instance.id
            print "Instance Type:\t\t" + instance.instance_type
            print "Launch Time: \t\t" + instance.launch_time
            print "==================================="

print "\nConnecting to Amazon S3...\n"
s3 = boto.connect_s3()

print "Retreiving bucket information...\n"
buckets = s3.get_all_buckets()

print "Current AWS S3 buckets:"
for bucket in buckets:
    print "\nBucket name: "
    print bucket.name

"""
line 8:     Connect to ec2 service using the boto method, which returns an EC2Connection object.
            My identity is verified with credentials that are stored in a config file in my
            /home directory called ~/.boto.

line 9:     Return a list of RegionInfo objects which contain information for all regions
            where an instance can be located.

line 11:    for loop to loop through all RegionInfo objects.

line 12:    make a connection to EC2 with the region parameter set to the current region from the loop.
            Returns an EC2Connection object for that region.

line 14:    Gets a list of Reservation objects from the region's EC2Connection.

line 16:    List comprehension to return the list of instances in this region.

line 18:    check if the list has less than one instance

line 22:    else, loop through each instance object, printing details of each

line 29:    make connection to s3 service. Returns an S3Connection object.

line 32:    Get list of all buckets. Returns a ResultSet object containing all buckets' info.

line 35:    Loop through all buckets.

"""








