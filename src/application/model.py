# choclately goodness model
# from flask_sqlalchemy import sqlalchemy as database
import json

import sqlite3


# import logging

# db_engine = None

class Model:

    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        try:
            # db_engine = database.create_engine("sqlite:///cocoa_flavors.sqlite")
            # return db_engine.connect()
            return sqlite3.connect('C:\\Users\\broderick1\\Documents\\choc-good-project\\cocoa_flavors')
        except sqlite3.Error as e:
            print(e)
        except:
            print("Database connection failed")

    def close(self):
        self.connection.close()

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
        sql_query = 'select company_name.*, bean_origin_type.* from bean_origin_type ' \
                   'INNER JOIN company_name on bean_origin_type.companyID = company_name.companyID;'

        # chocolate_tbl = database.Table('bean_origin_type', database.MetaData(self.connection), autoload=True)
        # chocolate_qry = database.select([chocolate_tbl])

        # print(chocolate_qry)

        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        record_set = cursor.fetchall()

        for record in record_set:
            (comid, company, location, barid, bar_name, bean_origin, coco_percent, bean_type, redudentid) = record
            record_list.append([company, location, bar_name, bean_origin, coco_percent, bean_type])

        record_list_json = json.dumps(record_list)

        return record_list_json

    def postUser(self, name, password):
        sqlQuery = "Insert INTO User (username, password, email) VALUES(?,?,?);"

        print(name + " " + password)
        cursor = self.connection.cursor()
        cursor.execute(sqlQuery, (name, password, "noemail@email.com"))

    def getUser(self, name, password):
        record_set = []
        sqlQuery = "Select username, password from user where " \
                   "password = %s and username = %s"

        cursor = self.connection.cursor()
        cursor.execute(sqlQuery, (name, password))
        record_set = cursor.fetchall()

        if record_set.count() == 0:
            return False
        else:
            return True

    """
    
        get selected chocolate bars by the manufactor
    """
    def getSelectedBars(self, company_name):
        sqlQuery = 'select company_name.*, bean_origin_type.* from bean_origin_type ' \
                   'INNER JOIN company_name on bean_origin_type.companyID = company_name.companyID ' \
                   'where company = ?;'

        record_list = []

        cursor = self.connection.cursor()
        cursor.execute(sqlQuery, (company_name,))
        record_set = cursor.fetchall()

        for record in record_set:
            (comid, company, location, barid, bar_name, bean_origin, coco_percent, bean_type, redudentid) = record
            record_list.append([company, location, bar_name, bean_origin, coco_percent, bean_type])

        record_list_json = json.dumps(record_list)

        return record_list_json