"""
Name: db_handler.py
Purpose: the db handler. uses sql\nosql sub classes.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""


class DBHandler:
    def __init__(self, handlers, logger):
        self.logger = logger
        self.handlers = handlers

    def query(self, command, handler_type):
        return self.handlers[handler_type].query(command)

    def insert(self, command, handler_type):
        self.handlers[handler_type].insert(command)


