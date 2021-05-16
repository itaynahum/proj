"""
Name: IDBHandler.py
Purpose: File containing interface which acts as an observer for different sql \nosql handlers.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""


class IDBHandler:
    def __init__(self, connection):
        self.connection = connection

    def query(self, command):
        raise NotImplementedError()

    def insert(self, command):
        raise NotImplementedError()
