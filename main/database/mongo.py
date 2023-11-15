import pymongo


def create_mongo(host: str, port: int) -> pymongo.MongoClient:
    client = pymongo.MongoClient(host, port)

    return client

