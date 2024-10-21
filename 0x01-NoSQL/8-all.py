#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    :return: A cursor containing the
    result of the find operation
    """
    return mongo_collection.find()
