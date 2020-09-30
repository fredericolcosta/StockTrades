

from abc import abstractmethod
from db.stocks_database import StocksDatabase


class DataRepository:
    """ 
    Data repository. 
  
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
    def __init__(self, username, password, address, port, db):
        self.database = StocksDatabase(username,password,address, port,db)

    """
    Add stock information to database

    Parameters: 
    stocks_json (dict): stock info provided by API in JSON
  
    Returns: 
    """
    def add_stocks_info(self, stocks_json):
        stocks = []
        for stock in stocks_json['chart']:
            stocks.append(stock)
        
        self.database.add_stocks(stocks)
        


        

    
