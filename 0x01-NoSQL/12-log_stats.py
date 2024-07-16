#!/usr/bin/env python3
"""This module implements a NoSQL DB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """This script provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx
    count_logs = mongo_collection.count_documents({})
    count_get = mongo_collection.count_documents({'method': 'GET'})
    count_post = mongo_collection.count_documents({'method': 'POST'})
    count_put = mongo_collection.count_documents({'method': 'PUT'})
    count_patch = mongo_collection.count_documents({'method': 'PATCH'})
    count_delete = mongo_collection.count_documents({'method': 'DELETE'})
    count_status = mongo_collection.count_documents({'path': '/status'})
    print('{} logs'.format(count_logs))
    print('Methods:')
    print('    method GET: {}'.format(count_get))
    print('    method POST: {}'.format(count_post))
    print('    method PUT: {}'.format(count_put))
    print('    method PATCH: {}'.format(count_patch))
    print('    method DELETE: {}'.format(count_delete))
    print('{} status check'.format(count_status))
