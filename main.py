# import pymongo
from pymongo import MongoClient
from jsonschema import validate
from validations import Validations
import json

cluster = MongoClient("mongodb+srv://audiofile:audiofile@cluster0.7ilyc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = cluster["AudioFile"]

collection_audiobook = database["AudioBook"]
collection_podcast = database["Podcast"]
collection_song = database["Song"]

file = open('create_song.json')
data = json.load(file)
print(data)

schema_check = Validations.get_schema(data)

if validate(instance=data, schema=schema_check) is None:
    insertable_data = data["records"]
    if data["audio_type"] == "Song":
        collection_song.insert_many(insertable_data)
    if data["audio_type"] == "Podcast":
        collection_podcast.insert_many(insertable_data)
    if data["audio_type"] == "AudioBook":
        collection_audiobook.insert_many(insertable_data)
else:
    print("bye")
# collection_audiobook.delete_many({})

