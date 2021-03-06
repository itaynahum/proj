"""
Name: consts.py
Purpose: File contains messages and queries used inside the program
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

LOGGER_CREATION = 'Successfully initialized logger...'
DATABASE_CONNECTION = 'Successfully connected to database {0}'
SLEEP_LOG = 'Program sleeps for {0} seconds...'
RUNNING_LOG = 'Running handler...'
SUCCESSFULLY_CREATED_TABLE = 'Successfully created table named {0} inside database {1}'
TABLE_ALREADY_EXISTS = 'Table named {0} already exists or an exception occurred...\r\n\tException: {1}'
SUCCESSFULLY_CREATED_DATABASE = 'Successfully created database named {0}'
DATABASE_ALREADY_EXISTS = 'Database named {0} already exists or an exception occurred...\r\n\tException:{1}'
NEW_FILES_COUNT = 'Found new {0} files inside {1}, now parsing and inserting...'
RELEVANT_FILE_INFO = 'Found relevant file information inside: {0}'
SUCCESSFULLY_REMOVED_FILE = 'Removed file from directory...'
INSERTION_ERROR = 'An error occurred while trying to update table or api...\r\n\tException: {0}'
FINISHED_PARSING_FILES = 'Finished parsing files. Continuing...'
ERROR_READING_FILES_DATA = 'An error occurred while reading files data...\r\n\tException: {0}'
SUCCESSFULLY_INSERTED_INTO_DATABASE = 'Successfully inserted files information into relevant format table...'

# SQL Commands
CREATE_JSON_TABLE = """
                        CREATE TABLE {0}.dbo.{1} (
                            timestamp varchar(120), 
                            name varchar(150), 
                            telemetry_id varchar(150), 
                            generated_number FLOAT)
                    """

CREATE_PCAP_TABLE = """
                        CREATE TABLE {0}.dbo.{1} (
                            
                        )
                    
                    """


CREATE_DATABASE = 'CREATE DATABASE {0}'

INSERT_INFORMATION = "INSERT INTO {0}.dbo.{1} {2} VALUES {3}"
# 0 - database 1 - table, 2 - fields, 3 - values
