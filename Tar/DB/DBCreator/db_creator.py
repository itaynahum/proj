"""
Name: db_creator.py
Purpose: The class which manages the creating of the tables. 
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

from proj.Utilities.consts import *


class DBCreator:
    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger

    def create_json_table(self, db_name, tablename):
        try:
            self.connection.execute(CREATE_JSON_TABLE.format(db_name, tablename))
            self.connection.commit()
            self.logger.debug(SUCCESSFULLY_CREATED_TABLE.format(tablename, db_name))
        except Exception as error:
            self.logger.error(TABLE_ALREADY_EXISTS.format(tablename, error))

    def create_pcap_table(self):
        raise NotImplementedError()

    def create_database(self, database_name):
        try:
            self.connection.execute(CREATE_DATABASE.format(database_name))
            self.logger.debug(SUCCESSFULLY_CREATED_DATABASE.format(database_name))
        except Exception as error:
            self.logger.error(DATABASE_ALREADY_EXISTS.format(database_name, error))
