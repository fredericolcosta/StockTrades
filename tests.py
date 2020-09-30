from db.data_repository import DataRepository
from api.data_extractor import DataExtractor


#TODO Handle api and db exceptions 

if __name__ == "__main__":
    url = 'https://cloud.iexapis.com/stable/stock/FB/batch'
    params = {'token':'pk_daeacff88d4d4fa58d0a79dbba45d7dd',
    'types':'chart', 'range': '1m', 'last':10}

    try:
        dt_ex = DataExtractor(url, params)
        json_response = dt_ex.get_json_response()
        print("Fetching info from API...")
    except Exception as e:
        print("There was an error acessing API:", e)
    else:
        dt_repo = None
        try:
            dt_repo = DataRepository("root","passroot321","localhost","3306","stock_trade")
            dt_repo.add_stocks_info(json_response)
        except Exception as e:
            print("There was an error acessing database:", e)
        finally:
            dt_repo.close_connection()
        


    #dt_repo.get_stocks_info()