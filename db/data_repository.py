from abc import abstractclassmethod


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
    Initializes database(creates tables)
    """
    @abstractclassmethod
    def initialize_db(self):
        pass

    """
    Add stock information to database
    """
    def add_stocks_info(self):
        pass
        

    
