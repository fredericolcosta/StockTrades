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
        
            response = requests.get(self.url_request,params=self.params, timeout=5)
            response.raise_for_status()
  
        
        
            json_response = response.json()
            return json_response


    
    
