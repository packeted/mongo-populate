
#!/usr/bin/python
#
# This script generates a linked set of MongoDB documents and inserts them in to your database.
# It was designed to help us populate a new customer account with example data that was linked to their account
# All these documents have "dummy" : True to allow for future identification and deletion
#
import sys
import pymongo
import uuid
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from dateutil import parser
import argparse

arg_parser = argparse.ArgumentParser(description='')

arg_parser.add_argument('--mongo-host', action="store", required=True)
arg_parser.add_argument('--mongo-port', action="store", type=int, required=True)
arg_parser.add_argument('--mongo-db', action="store", required=True)
arg_parser.add_argument('--mongo-username', action="store", required=True)
arg_parser.add_argument('--mongo-password', action="store", required=True)
arg_parser.add_argument('--org-id', action="store", required=True)
arg_parser.add_argument('--user-id', action="store", required=True)
arg_parser.add_argument('--group-id', action="store", required=True)
parsed = arg_parser.parse_args()

auth = ''
if parsed.mongo_username:
	auth = '{}:{}@'.format(parsed.mongo_username, parsed.mongo_password)

mongo_connect_string = "mongodb://{}{}:{}/".format(auth, parsed.mongo_host, parsed.mongo_port or 27017)

# Initiate connection to MongoDB
client = MongoClient(mongo_connect_string)
db = getattr(client, parsed.mongo_db)

# read these from the command line
orgid = parsed.org_id
userid = parsed.user_id
groupid = parsed.group_id

# Generate new unique IDs for the new dummy objects and store so documents can be linked
customer1_id = ObjectId()
project1_id = ObjectId()

# Create JSON objects to insert
customer_1 =		{
				    "_id" : ObjectId(customer1_id),
				    "createdAt" : parser.parse("2017-07-27T17:54:35.553+0000"),
				    "updatedAt" : parser.parse("2017-07-27T23:46:07.715+0000"),
				    "dob" : parser.parse("1950-01-02T08:00:00.000+0000"),
				    "gender" : "male",
				    "last" : "Customer",
				    "first" : "Test",
				    "hidden" : False,
				    "inactive" : False,
				    "dummy" : True,
				    "verification" : {
				        "email" : {
				            "verified" : "testcustomer1@domain.com",
				            "verifiedBy" : ObjectId(userid),
				            "verifiedAt" : parser.parse("2017-07-27T23:46:07.707+0000")
				        },
				        "phone" : {
				            "verified" : None,
				            "verifiedBy" : None,
				            "verifiedAt" : None
				        },
				        "link" : {
				            "time" : "2017-07-27T17:54:35.563Z"
				        }
				    },
				    "fields" : [

				    ],
				    "preference" : [
				        "Email"
				    ],
				    "zip" : None,
				    "state" : None,
				    "city" : None,
				    "address" : None,
				    "language" : "english",
				    "phone" : 5102205137.0,
				    "email" : "testpatient@revs.com",
				    "mrn" : "34567890",
				    "owners" : [
				        ObjectId(userid)
				    ],
				    "groups" : [
				        ObjectId(groupid)
				    ],
				    "organization" : ObjectId(orgid),
				    "__v" : 0,
				    "resolved" : {

				    }
				}

project_1 =	{ 
				    "_id" : ObjectId(project1_id), 
				    "createdAt" : parser.parse("2017-07-27T17:55:36.308+0000"), 
				    "updatedAt" : parser.parse("2017-08-03T23:09:05.489+0000"), 
				    "type" : "My First Project", 
				    "customer" : ObjectId(customer1_id), 
				    "owner" : ObjectId(userid), 
				    "hidden" : False, 
				    "dummy" : True,
				    "device" : None, 
				    "location" : None, 
				    "operationDate" : parser.parse("2016-07-26T07:00:00.000+0000"), 
				    "stage" : "post-treatment", 
				    "entry" : "post-treatment", 
				    "team" : [
				        ObjectId(userid)
				    ], 
				    "primaryOwner" : ObjectId(userid), 
				    "__v" : 22
				}



document1_1 =		{ 
				    "_id" : ObjectId(), 
				    "createdAt" : parser.parse("2016-02-01T20:35:11.262+0000"), 
				    "updatedAt" : parser.parse("2017-08-11T17:29:38.676+0000"), 
				    "uniqueUrl" : uuid.uuid4(), 
				    "type" : ObjectId("596d3a0fb189b8001d0431c3"), 
				    "project" : ObjectId(project1_id), 
				    "intake" : False, 
				    "hidden" : False, 
				    "dummy" : True,
				    "scheduleIndex" : 9, 
				    "__v" : 1
				}

# insert documents
db.customers.insert_one(customer_1)
db.projects.insert_one(project_1)
db.documents.insert_one(document1_1)

# Print Documents instead
# print(customer_1)
# print(project_1)
# print(document1_1)