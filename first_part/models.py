
from mongoengine import Document
from mongoengine.fields import  ListField, StringField, ReferenceField


class Author(Document):
    name = StringField(max_length=50, required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField('Author')
    quote = StringField(required=True)





