"""
Name: main.py
Purpose: The main constructor of the program
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

from Config.config import *
from Utilities.consts import *
from Tar.DB.DBConnection.sql_connection import SqlConnection
from Tar.DB.DBHandler.db_handlers import SqlHandler
from Utilities.logger import InitRotatingLogger
from Tar.Root.MainHandler.handler import Handler
from Tar.Root.FileHandlers.pcaphandler import PcapHandler
from Tar.Root.FileHandlers.jsonhandler import JsonHandler
from Tar.DB.DBHandler.db_handler import DBHandler
from Tar.Root.Runner.runner import Runner
from Utilities.utilities import validate_folders
from Tar.DB.DBCreator.db_creator import DBCreator

validate_folders([TARSIUM_INPUT_PATH, LOGFILE_DIR])


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
    logger = InitRotatingLogger()
    logger = logger.get_logger()
    logger.info(LOGGER_CREATION)
    master_db_connection = SqlConnection(DRIVER, SERVERNAME, ROOT_DBNAME).connect()
    dbcreator = DBCreator(connection=master_db_connection, logger=logger)
    dbcreator.create_database(DBNAME)
    _create_tables(dbcreator)
    connection = SqlConnection(DRIVER, SERVERNAME, DBNAME).connect()
    logger.info(DATABASE_CONNECTION.format(DBNAME))
    filehandlers = dict(zip(SUPPORTED_INPUT_FILES_TYPES,
                            [JsonHandler(), PcapHandler()]))
    db_handlers = {
        'sql': SqlHandler(connection=connection)
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
