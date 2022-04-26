#!/usr/bin/env python3
"""my first NoSQL database"""
if __name__ == "__main__":
    def list_all(mongo_collection):
        """list all documents in a collection"""
        documents = []
        res = mongo_collection.find({})
        for i in res:
            documents.append(i)
        return documents
