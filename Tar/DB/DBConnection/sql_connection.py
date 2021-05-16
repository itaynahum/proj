"""
Name: sql_connection.py
Purpose: file containing class which handles the sql connection method.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import pyodbc

from Taroot.Interfaces.IDBConnection.mssql_connection import ISqlConnection


class SqlConnection(ISqlConnection):
    """
    Class which creates connection objects.
    """
    def __init__(self, driver, servername, dbname, trusted_connection=True):
        super().__init__(driver, servername, dbname, trusted_connection)
    
    def connect(self):
        connection = pyodbc.connect(
            f"Driver={{{self.driver}}};"
            f"Server={self.servername};"
            f"Database={self.dbname};"
            "Trusted_Connection=yes;", autocommit=True)

        return connection.cursor()
