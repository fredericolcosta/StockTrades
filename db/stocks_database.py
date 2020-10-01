from sqlalchemy import exc, create_engine
from sqlalchemy.orm import sessionmaker
from db.stock import Stock, Base


class StocksDatabase():
    """
    Database handler 

    Creates connection and interface with database(Engine)
    and defines Session factory class for new Session objects
    to handle database

    Parameters: 
    username (string): username
    password(string): password to access database
    address(string): address of host
    db(string): name of database schema

    Returns: 
    """

    def __init__(self, username, password, address, port, db):
        self.engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(
            username,
            password,
            address,
            port,
            db))

        self.Session = sessionmaker(bind=self.engine)
        self.Session.configure(bind=self.engine)

    """
    Closes connection to database, disposing engine
    """

    def close_conn(self):
        self.engine.dispose()

    """
    Database initializer 

    Creates tables registed in Metadata

    Parameters: 
  
    Returns: 
    """

    def initialize_db(self):
        Base.metadata.create_all(self.engine)

    """
    Adds Mapped Objects 'Stocks' to database

    Parameters: 
    stocks (dict[]): list of stocks info provided by API 
  
    Returns: 
    """

    def add_stocks(self, stocks):
        # Creates tables that do not exist
        self.initialize_db()

        # Defines which information to fetch from json dict
        stock_attributes = ('added', 'date', 'open', 'close', 'high', 'low',
                            'volume', 'change', 'changePercent', 'label', 'changeOverTime')

        # Retrieves a connection from pool of connections (Session)
        session = self.Session()

        # Goes through stock info on json object
        for stock_info in stocks:
            # Unpacks JSON stock info to Mapped Class 'Stock'
            # filtering unnecessary data
            stock = Stock(
                **{i: stock_info[i] for i in stock_attributes if i in stock_info})

            # Adds or updates stock information
            session.merge(stock)

        try:
            session.commit()
        except exc.SQLAlchemyError:
            session.rollback()
            print(
                "Error: There was a problem in adding info to database.\n Rolling back...")
            raise
        else:
            print("Success: Added stock information to database")

    """
    Prints stock information from database

    Parameters: 
  
    Returns: 
    """

    def show_stocks_info(self):
        # Fetches connection from pool
        session = self.Session()

        # Queries database for stock info
        for added, date, open, close, high, low, volume, change, changePercent, label, ChangeOverTime in session.query(Stock.added,
                                                                                                                       Stock.date, Stock.open,
                                                                                                                       Stock.close, Stock.high, Stock.low,
                                                                                                                       Stock.volume, Stock.change, Stock.changePercent,
                                                                                                                       Stock.label, Stock.changeOverTime).order_by(Stock.added):

            stock_info = (added, date, open,
                          close, high, low,
                          volume, change, changePercent, label, ChangeOverTime)
