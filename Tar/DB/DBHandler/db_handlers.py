"""
Name: handlers.py
Purpose: The sql\nosql handlers classes.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""


from proj.Tar.Interfaces.IHandler.IDBHandler import IDBHandler


class NoSqlHandler(IDBHandler):
    def __init__(self, connection):
        super().__init__(connection)

    def insert(self, command):
        raise NotImplementedError()

    def query(self, command):
        raise NotImplementedError()


class SqlHandler(IDBHandler):
    def __init__(self, connection):
        super().__init__(connection)

    def insert(self, command):
        command_body, values = command[0], command[1]
        self.connection.execute(command_body, values)
        self.connection.commit()

    def query(self, command):
        return self.connection.execute(command)
