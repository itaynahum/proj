"""
Name: sql_connection.py
Purpose: file containing class which handles the sql connection method.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import pyodbc

from Tar.Interfaces.IDBConnection.mssql_connection import Connection


class SqlConnection(Connection):
    """
    Class which creates connection objects.
    """
    def __init__(self, driver, servername, dbname, trusted_connection=True):
        self.driver = driver
        self.servername = servername
        self.dbname = dbname
        self.trusted_connection = trusted_connection
    
    def connect(self, autocommit=True):
        connection = pyodbc.connect(
            f"Driver={{{self.driver}}};"
            f"Server={self.servername};"
            f"Database={self.dbname};"
            "Trusted_Connection=yes;", autocommit=autocommit)

        return connection.cursor()
