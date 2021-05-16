"""
Name: main.py
Purpose: The main constructor of the program
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""


class ISqlConnection:
    """
    Sql connection interface.
    """
    def __init__(self, driver, servername, dbname, trusted_connection=True):
        self.driver = driver
        self.servername = servername
        self.dbname = dbname
        self.trusted_connection = trusted_connection 
    
    def connect(self):
        raise NotImplementedError()
