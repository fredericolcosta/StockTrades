from db.data_repository import DataRepository
from api.data_extractor import DataExtractor

if __name__ == "__main__":
    url = 'https://cloud.iexapis.com/stable/stock/FB/batch'
    params = {'token':'pk_daeacff88d4d4fa58d0a79dbba45d7dd',
    'types':'chart', 'range': '1m', 'last':10}

    dt_ex = DataExtractor(url, params)
    json_response = dt_ex.get_json_response()
    
    dt_repo = DataRepository("root","passroot321","localhost","3306","stock_trade")
    dt_repo.add_stocks_info(json_response)

   