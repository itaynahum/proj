"""
Name: handler.py
Purpose: contains a class which manages all the other objects supplied - DIP.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""
import os

from proj.Utilities.utilities import validate_types, remove_file
from proj.Config.config import JSON_TABLE_NAME, SUPPORTED_INPUT_FILES_TYPES, DBNAME
from proj.Utilities.consts import *

EXTENSION_INDEX = 1
FIELDS_INDEX = 0
VALUES_INDEX = 1


class Handler:
    """
    This class knows how to handle insertions into
    multiple databases and handle multiple file types.
    """
    def __init__(self, filepath, readmode, filehandlers, dbhandlers, logger):
        self.filepath = filepath
        self.filehandlers = filehandlers
        self.dbhandlers = dbhandlers
        self.readmode = readmode
        self.logger = logger

    def insert_data(self, formatted_data):
        """
        functions which uses the selected sql server and inserts data
        :param formatted_data: The data modified before insertions. Contains fields and values.
        :return: None
        """
        for data_tuple in formatted_data:
            try:
                fields, values = data_tuple[FIELDS_INDEX], data_tuple[VALUES_INDEX]
                self.dbhandlers.insert(command=(INSERT_INFORMATION.format(DBNAME, JSON_TABLE_NAME, fields), values),
                                       handler_type='sql')
            except Exception as error:
                self.logger.error(INSERTION_ERROR.format(error))

    def _wrap_data(self, filepath):
        """
        Gets specific file path and assumes which file type it is, and by that it gets treated properly.
        Reads data, understands which type and then by that it creates the object.
        :param filepath: The path of the file
        :return: Two tuples contains field names and values, ready for insertion.
        """
        try:
            with open(filepath, self.readmode) as opened_file:
                filename, filesextension = os.path.splitext(filepath)
                files_data = opened_file.read()
                fields, values = self.filehandlers[filesextension[EXTENSION_INDEX:]].handle(files_data)
                return fields, values
        except (IOError, IndexError, AttributeError) as error:
            self.logger.error(ERROR_READING_FILES_DATA.format(error))

    def _get_input_files_list(self):
        """
        Generator which passes over all the files in the path supplied.
        :return: Yields single paths.
        """
        for inputted_file in os.listdir(self.filepath):
            yield os.path.join(self.filepath, inputted_file)

    @validate_types(SUPPORTED_INPUT_FILES_TYPES)
    def _parse_data(self, files_list):
        """
        Function responsible for the insertions and ordered list creation.
        :param files_list: List of files.
        :return: None
        """
        formatted_data = list()
        for f in files_list:
            formatted_data.append(self._wrap_data(f))
            self.logger.debug(RELEVANT_FILE_INFO.format(f))
            remove_file(f)
            self.logger.debug(SUCCESSFULLY_REMOVED_FILE)
        self.insert_data(formatted_data)

    def handle(self):
        files_list = list(self._get_input_files_list())
        self.logger.info(NEW_FILES_COUNT.format(len(files_list), self.filepath))
        self._parse_data(files_list)
        self.logger.info(FINISHED_PARSING_FILES)
