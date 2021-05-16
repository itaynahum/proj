"""
Name: consts.py
Purpose: File contains messages and queries used inside the program
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

LOGGER_CREATION = 'Successfully initialized logger...'
DATABASE_CONNECTION = 'Successfully connected to {}'
SLEEP_LOG = 'Program sleeps for {} seconds...'
RUNNING_LOG = 'Running handler...'

# SQL Commands
CREATE_JSON_TABLE = '''
                                 CREATE TABLE {0}.dbo.{1} (
                                        timestamp DATETIME NOT NULL ,
                                        name NVARCHAR NOT NULL ,
                                        telemetry_id NVARCHAR NOT NULL ,
                                        generated_number FLOAT NOT NULL 
                                );
                    '''

CREATE_DATABASE = 'CREATE DATABASE {0}'

INSERT_INFORMATION = """INSERT INTO {0}.dbo.{1} {2} VALUES (?,?,?,?)"""
# 0 - database 1 - table, 2 - fields, 3 - values
