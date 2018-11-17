from pymongo import MongoClient
from rhymer import Rhymer

def main():
    DB_NAME = "test_db"
    COLLECTION_NAME = "lyrics_collection"
    client = MongoClient()
    collection = client.get_database(DB_NAME).get_collection(COLLECTION_NAME)
    rhymer = Rhymer(collection)
    rhymer.create_markov()

main()