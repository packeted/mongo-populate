# mongo-populate
A way to populate MongoDB with linked example documents

### Why this was created

As we added new customers to our platform, we needed a great on-boarding experience but soon realized it would be pretty bare without any initial data. We use MongoDB and needed a way to create a standardized set of example documents for each new customer, all linked to their account but not conflicting with any of the other IDs in the database. I searched high and low for an existing solution but could find nothing that would set up the linkages we needed.

We created the example documents for one account and then exported the JSON. We then created this simple Python script that uses pymongo to connect to take inputs (the existing IDs associated with our new customer account) and then generate the example documents with the input IDs and new IDs where necessary. 

In this example script only three documents are created, one in each collection. The script we use generates and inserts 40 documents so is much longer but uses exactly the same principles. 

### Usage

Adapt for your own purpose namely IDs that can be passed from the command line and the documents you want to create and where you want them inserted.
Requires pymongo to be installed.
Test first by printing your documents, then try inserting in to a friendly test database before touching anything critical!

```
python mongo-populate.py [-h] --mongo-host MONGO_HOST --mongo-port MONGO_PORT
                         --mongo-db MONGO_DB --mongo-username MONGO_USERNAME
                         --mongo-password MONGO_PASSWORD --org-id ORG_ID
                         --user-id USER_ID --group-id GROUP_ID
```

### Acknowledgements

Thanks goes to Kevin Matuleff and realmbit without whom this wouldn't have been possible.
