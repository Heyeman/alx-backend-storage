def list_all(mongo_collection):
    l = []
    res = mongo_collection.find({})
    for i in res:
        l.append(i)
    return l