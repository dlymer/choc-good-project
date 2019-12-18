# choclately goodness model
import json
import flask_sqlalchemy as database

db_engine = None


class Model:

    def __init__(self):
        self.connection = connect()

    """
        Hello world
        
        test method to check that model class works!
    """
    def getHelloWorld(self):
        return "Hello World!"

    """
        get Chocolate Bars
        
        Returns all chocolate bars found in the database as a list of chocolate bars
         
    """
    def get_ChocolateBars(self):
        record_list = []
        sql_query = "Select"
        record_set = database.select([])

        for record in record_set:
            (company, bar_name, ref, review_date, coco_percent, location, rating,
             bean_type, broad_origin) = record
            record_list.append([company, bar_name, ref, review_date, coco_percent, location, rating,
                                bean_type, broad_origin.isoformat()])

        record_list_json = json.dumps(record_list)
        return record_list_json


def connect():
    try:
        db_engine = database.create_engine("")
        return db_engine.connect()
    except:
        print("Database connection failed")


def close():
    db_engine.close()
