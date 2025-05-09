#!/usr/bin/en python3
"""MongoDB operations with python"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of all documents with the given school name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
