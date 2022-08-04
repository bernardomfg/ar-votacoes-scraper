from typing_extensions import Required
from mongoengine import *

class File(Document):
    file_url = URLField()
    