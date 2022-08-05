from mongoengine import *

class File(Document):
    file_url = URLField(required=True)
    isParsed = BooleanField()
    localFilePath = StringField()


    