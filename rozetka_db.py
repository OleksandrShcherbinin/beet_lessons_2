from peewee import (
    Model,
    SqliteDatabase,
    CharField,
    ForeignKeyField,
    IntegerField,
)


db = SqliteDatabase('rozetka.db')


class BaseModel(Model):

    class Meta:
        database = db


class Price(BaseModel):
    price = IntegerField()
    old_price = IntegerField(null=True)


class Product(BaseModel):
    name = CharField(max_length=255)
    reviews = CharField(max_length=50, null=True)
    promo = CharField(max_length=30, null=True)
    availability = CharField(max_length=50, null=True)
    rating = CharField(max_length=30, null=True)
    price = ForeignKeyField(Price)


class Image(BaseModel):
    product = ForeignKeyField(Product)
    url = CharField(max_length=255)


if __name__ == '__main__':
    db.create_tables([Price, Product, Image])
