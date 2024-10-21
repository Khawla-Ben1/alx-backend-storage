#!/usr/bin/env python3
"""
function that inserts a new document in
a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    :return: _id of the newly inserted document
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
