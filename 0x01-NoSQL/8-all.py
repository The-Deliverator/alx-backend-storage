#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""
import pymongo


def list_all(mongo_collection):
    """Returns:
    List of documents or an empty list if no documents exist
    """
    return list(mongo_collection.find()) or []
