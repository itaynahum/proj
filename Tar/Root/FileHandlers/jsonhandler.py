"""
Name: jsonhandler.py
Purpose: Object which handles json files data.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import json

from proj.Tar.Interfaces.IHandler.IFileHandler import IFileHandler


class JsonHandler(IFileHandler):
    """
    Object which handles json data.
    """
    @staticmethod
    def _get_json_serialized_data(data):
        return json.loads(data)

    def handle(self, files_data):
        json_data = self._get_json_serialized_data(files_data)
        field_names, field_values = tuple(json_data.keys()), tuple(json_data.values())
        return field_names, field_values
