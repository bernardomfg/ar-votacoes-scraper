# model/file.py
from mongoengine import Document, StringField, DateTimeField, DateField, URLField, BooleanField
class File(Document):
    file_url = URLField(required=True)
    votingDate = DateField()
    filename = StringField()
    isParsed = BooleanField()
    localFilePath = StringField(required=True, default="")
    created = DateTimeField()


    