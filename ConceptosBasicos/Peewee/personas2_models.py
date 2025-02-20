from peewee import *

database = SqliteDatabase('people.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    birthday = DateField()
    name = CharField()

    class Meta:
        table_name = 'person'

class Pet(BaseModel):
    animal_type = CharField()
    name = CharField()
    owner = ForeignKeyField(column_name='owner_id', field='id', model=Person)

    class Meta:
        table_name = 'pet'

