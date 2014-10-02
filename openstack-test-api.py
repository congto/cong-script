#!/usr/bin/python

import argparse
import getopt
import json
import sys
import urllib2

def getToken(url, osuser, ostenant, ospassword):

    """ 
    Returns a token to the user given a tenant, 
    user name, password, and OpenStack API URL. 
    """
    url = url + '/tokens'
    tokenRequest = urllib2.Request(url)
    tokenRequest.add_header("Content-type", "application/json")
    jsonPayload = json.dumps({'auth' : {'tenantName' : ostenant, 'passwordCredentials' : {'username' : osuser, 'password' : ospassword}}})
    
    request = urllib2.urlopen(tokenRequest, jsonPayload)
    json_data = json.loads(request.read())
    
    request.close()
    return json.dumps(json_data)

# Build our required arguments list
parser = argparse.ArgumentParser()
mandatory = parser.add_argument_group("mandatory")
mandatory.add_argument("-l", "--login", help="The administrative user for your OpenStack installation", type=str)
mandatory.add_argument("-p", "--password", help="The administrative user's password", type=str)
mandatory.add_argument("-t", "--tenant", help="The administrative user's tenant / project", type=str)
mandatory.add_argument("-u", "--url", help="The Keystone API endpoint from running, 'nova endpoints'", type=str)
args = parser.parse_args()

# Validate arugments were given
if type(args.url) != type(str()):
    sys.stderr.write('Invalid URL: %s\n' % args.url)
    parser.print_help()
    sys.exit(2)
if type(args.tenant) != type(str()):
    sys.stderr.write('Invalid tenant: %s\n' % args.tenant)
    parser.print_help()
    sys.exit(2)
if type(args.password) != type(str()):
    sys.stderr.write('Invalid password: %s\n' % args.password)
    parser.print_help()
    sys.exit(2)
if type(args.login) != type(str()):
    sys.stderr.write('Invalid login: %s\n' % args.login)
    parser.print_help()
    sys.exit(2)
    
# Since we return a raw JSON payload from getToken,
# we need to load it into a readable object.
adminToken = json.loads(getToken(args.url, args.login, args.tenant, args.password))

# Access the token portion of the JSON payload and grab the token and tenant ID
adminTokenID = adminToken['access']['token']['id']
adminTokenTenantID = adminToken['access']['token']['tenant']['id']

for item in adminToken['access']['serviceCatalog']:
    """ 
    The "name" of each OpenStack service catalog item from
    the item list changed between versions.  Things like 
    "glance" became "volume" and "keystone" became "identity".  
    You will need to update this based on your installation.
    """
    if item['name'] == "nova": 
        adminNovaURL = item['endpoints'][0]['adminURL']
    if item['name'] == "glance":
        adminGlanceURL = item['endpoints'][0]['adminURL']
    if item['name'] == "nova-volume":
        adminVolumeURL = item['endpoints'][0]['adminURL']
    if item['name'] == "ec2":
        adminEc2URL = item['endpoints'][0]['adminURL']
    if item['name'] == "swift":
        adminSwiftURL = item['endpoints'][0]['adminURL']
    if item['name'] == "keystone":
        adminAuthURL = item['endpoints'][0]['adminURL']

print "------ Admin information ------"
print "Token ID = ", adminTokenID
print "Tenant ID = ", adminTokenTenantID
print "Nova URL = ", adminNovaURL
print "Glance URL = ", adminGlanceURL
print "Volume URL = ", adminVolumeURL
print "EC2 URL = ", adminEc2URL
print "Swift URL = ", adminSwiftURL
print "Keystone URL = ", adminAuthURL
print "------ End Admin info ---------"

#Source : http://four-eyes.net/2012/11/openstack-api-python-script-example/
