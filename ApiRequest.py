import requests

# The purpose of this class is to send API requests and save the response JSON #
class ApiRequest:

    # Constructor
    def __init__(self):
        self.__responseData = None
        return
    
    # Public Methods #

    # The purpose of this method is to send a GET request #
    # Params:
    #   link -> (str) the url to send the request to
    def SendGetRequest(self, link: str):
        response = requests.get(link)
        self.__responseData = response.json()
        return
    
    # The purpose of this method is to send a POST request #
    # Params:
    #   link -> (str) the url to send the request to
    #   postData -> (dict) dictionary that holds the data to send in the post request
    def SendPostRequest(self, link: str, postData: dict, headers: dict):
        response = requests.post(link, json=postData, headers=headers)
        self.__responseData = response.json()
        return
    
    # The purpose of this method is to return the JSON data from the request #
    def GetReturnData(self):
        return self.__responseData

    # Private Methods #
