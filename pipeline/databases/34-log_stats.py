#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
nginx_collection = db.nginx

print(f"{nginx_collection.count_documents({})} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = nginx_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")
