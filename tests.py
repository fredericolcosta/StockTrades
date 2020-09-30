from datetime import datetime
from db.data_repository import DataRepository
from api.data_extractor import DataExtractor
import logging
from dotenv import load_dotenv
import os


def log_error(type):
        logging.basicConfig(filename='errors.log',level=logging.DEBUG)
        logging.info(datetime.now())
        logging.exception(type)

def save_stocks(url, params, username,password,address, port,database):
    try:
        dt_ex = DataExtractor(url, params)
        json_response = dt_ex.get_json_response()
        print("Fetching info from API...")
    except Exception as e:
        print("There was an error acessing API:", e)
        log_error("API")
    else:
        dt_repo = None
        try:
            dt_repo = DataRepository(username,password,address, port,database)
            dt_repo.add_stocks_info(json_response)
        except Exception as e:
            print("There was an error acessing database:", e)
            log_error("DATABASE")
        finally:
            dt_repo.close_connection()


if __name__ == "__main__":
    #Load with your values
    load_dotenv()
    token = os.getenv("TOKEN")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    address = os.getenv("ADDRESS")
    port = os.getenv("PORT")
    database = os.getenv("DATABASE")
    token = os.getenv("TOKEN")

    url = 'https://cloud.iexapis.com/stable/stock/FB/batch'
    params = {'token':token,
    'types':'chart', 'range': '1m', 'last':10}
    
    save_stocks(url, params, username, password, address, port, database)


