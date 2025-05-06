#!/usr/bin/env python3
"""Module containing function that inserts a new document in a collection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the collection based on keyword arguments.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
