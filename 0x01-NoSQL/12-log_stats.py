#!/usr/bin/env python3
"""MongoDB Operations with Python"""
from pymongo import MongoClient


def get_nginx_stats():
    """gives stats about Ngin logs stored in MongoDB"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check logs")


if __name__ == "__main__":
    get_nginx_stats()
