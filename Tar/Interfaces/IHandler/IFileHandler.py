"""
Name: IFileHandler.py
Purpose: File containing interface which acts as an observer of pcaphandler and jsonhandler
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""


class IFileHandler:
    """
    Interface of a file handler. 
    """
    def handle(self, files_data):
        raise NotImplementedError()
