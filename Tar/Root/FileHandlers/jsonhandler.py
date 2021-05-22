"""
Name: jsonhandler.py
Purpose: Object which handles json files data.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import json

from Tar.Interfaces.IHandler.IFileHandler import IFileHandler


class JsonHandler(IFileHandler):
    """
    Object which handles json data.
    """
    @staticmethod
    def _get_json_serialized_data(data):
        return json.loads(data)

    @staticmethod
    def get_splitted_dict(dictionary):
        return tuple(dictionary.keys()), tuple(dictionary.values())

    def handle(self, files_data):
        json_data = self._get_json_serialized_data(files_data)
        field_names, field_values = self.get_splitted_dict(json_data)
        return field_names, field_values
