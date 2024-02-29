#!/usr/bin/env python3
"""placeholder"""

def schools_by_topic(mongo_collection, topic):
    """placeholder"""
    return list(mongo_collection.find({"topics": topic}))
