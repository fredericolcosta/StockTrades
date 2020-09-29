from sqlalchemy import *

class Database:
    """ 
    Database abstract class. 
  
    Defines methods to configure and handle database
    """
    
    """
    Configures database access info

    Parameters: 
    username (string): username
    password(string): password to access database
    address(string): address of host
    db(string): name of database schema
  
    Returns: 

    """
    def __init__(self, username, password, address, db):
        self.username = username
        self.password = password
        self.address = address 
        self.db_name = db

    """
    Creates database connection
    """
    def create_conn(self):
        pass

    """
    Closes database connection
    """
    def close_conn(self):
        pass

    """
    Initializes database(creates tables)
    """
    def initialize_db(self):
        pass

    """
    Add stock information to database
    """
    def add_stock_info(self):
        pass

    
