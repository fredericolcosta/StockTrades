from sqlalchemy import *
from db_config import Database
from stock import Base

class DatabaseAlchemy(Database):

    def __init__(self):
        super().__init__()
    
    def create_conn(self):
        self.engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(
            self.username, 
            self.password, 
            self.address, 
            self.port, 
            self.db))


    def initialize_db(self):
        Base.metadata.create_all(self.engine)
        


    