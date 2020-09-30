import requests

class DataExtractor:
    """
    Handler of communication with API

    Parameters:
    url (string): url of API 
    params (dict): query parameters
    """
    def __init__(self, url, params):
        self.url_request = url 
        self.params = params

    """
    Request data from API 

    Parameters:
 
    Returns:
    json_response (dict): JSON data
    """
    def get_json_response(self):
        try:
            response = requests.get(self.url_request,params=self.params, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print ("HTTP Error:",err)
        except requests.exceptions.ConnectionError as err:
            print ("Connection Error:",err)
        except requests.exceptions.Timeout as err:
            print ("Timeout Error:",err)
        except requests.exceptions.RequestException as err:
            print ("Error:",err)
        
        else:
            json_response = response.json()
            return json_response

if __name__ == "__main__":
    url = 'https://cloud.iexapis.com/stable/stock/FB/batch'
    params = {'token':'pk_daeacff88d4d4fa58d0a79dbba45d7dd',
    'types':'chart', 'range': '1m', 'last':10}
    dt_ex = DataExtractor(url, params)

    json_response = dt_ex.get_json_response()
    print(json_response)

    
