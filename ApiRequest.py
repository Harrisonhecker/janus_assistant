import requests
import json

class ApiRequest:

    # Constructor
    def __init__(self):
        self.__responseData = None
        return
    
    # Public Methods #
    def SendRequest(self, link):
        response = requests.get(link)
        self.__responseData = response.json()
        return
    
    def GetReturnData(self):
        return self.__responseData

    # Private Methods #
