#!/usr/bin/env python3
"""my docs"""


def schools_by_topic(mongo_collection, topic):
    """filters schools by topic"""
    return [e for i in mongo_collection.find({"topic": {"$in": [topic]}})]
