from mongoengine import *

class File(Document):
    file_url = URLField(required=True)
    filename = StringField()
    isParsed = BooleanField()
    localFilePath = StringField()
    created = DateTimeField()


    