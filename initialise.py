from pymongo import MongoClient
from rhymer import Rhymer

def main():
    DB_NAME = "hiphop"
    COLLECTION_NAME = "lyrics_collection"
    client = MongoClient()
    collection = client.get_database(DB_NAME).get_collection(COLLECTION_NAME)
    r = Rhymer(collection)
    r.create_markov()

main()