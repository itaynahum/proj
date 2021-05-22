
from Tar.Interfaces.IDBConnection.mssql_connection import Connection


class NoSqlConnection(Connection):
    """
    Class which creates connection objects.
    """
    def __init__(self):
        pass

    def connect(self):
        pass
