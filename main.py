"""
Name: main.py
Purpose: The main constructor of the program
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""
import threading
import Tar.Root.API.api as api

from Config.config import *
from Utilities.consts import *
from Tar.DB.DBConnection.sql_connection import SqlConnection
from Tar.DB.DBConnection.nosql_connection import NoSqlConnection
from Tar.DB.DBHandler.db_handlers import SqlHandler, NoSqlHandler
from Utilities.logger import InitRotatingLogger
from Tar.Root.MainHandler.handler import Handler
from Tar.Root.FileHandlers.pcaphandler import PcapHandler
from Tar.Root.FileHandlers.jsonhandler import JsonHandler
from Tar.DB.DBHandler.db_handler import DBHandler
from Tar.Root.Runner.runner import Runner
from Utilities.utilities import validate_folders
from Tar.DB.DBCreator.db_creator import DBCreator

THREAD = threading.Thread


def _create_tables(dbcreator_obj):
    """
    Function responsible for table creations
    :param dbcreator_obj: The db creator object supplied
    :return: None
    """
    for _, tablename in TABLE_NAMES.items():
        dbcreator_obj.create_json_table(DBNAME, tablename)


def main():
    """
    Main Builder
    :return: None
    """
    validate_folders([TARSIUM_INPUT_PATH, LOGFILE_DIR])
    # initialize logger
    logger = InitRotatingLogger()
    logger = logger.get_logger()
    logger.info(LOGGER_CREATION)
    # start api
    THREAD(target=api.start_app, args=(logger,)).start()
    # db procedures
    master_db_connection = SqlConnection(DRIVER, SERVERNAME, ROOT_DBNAME).connect()
    dbcreator = DBCreator(connection=master_db_connection, logger=logger)
    dbcreator.create_database(DBNAME)
    _create_tables(dbcreator)
    sql_connection = SqlConnection(DRIVER, SERVERNAME, DBNAME).connect(autocommit=False)
    nosql_connection = NoSqlConnection().connect()
    logger.info(DATABASE_CONNECTION.format(DBNAME))
    filehandlers = dict(zip(SUPPORTED_INPUT_FILES_TYPES,
                            [JsonHandler(), PcapHandler()]))
    # create objects
    db_handlers = {
        'sql': SqlHandler(connection=sql_connection),
        'nosql': NoSqlHandler(connection=nosql_connection)
    }
    dbhandlers = DBHandler(
        logger=logger,
        handlers=db_handlers
    )
    handler = Handler(
        filepath=TARSIUM_INPUT_PATH,
        dbhandlers=dbhandlers,
        filehandlers=filehandlers,
        logger=logger,
        readmode=INPUT_FILES_READMODE
    )
    runner = Runner(
        handler=handler,
        logger=logger,
        timeout=TIMEOUT
    )
    runner.run()


if __name__ == '__main__':
    main()
