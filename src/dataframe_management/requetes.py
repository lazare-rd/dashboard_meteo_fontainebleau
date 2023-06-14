import requests
import json

class Request_Manager : 

    #
    # Constructor
    # self.urls : dict( city : [urls] ) (urls as str)
    # self.data : dict( city : [json] ) (json as str)
    #
    def __init__(self) :
        self.__urls = {}
        self._data = {}

    @property
    def data(self):
        return self._data 

    #
    # Manages the updating and/or the instatiation of a key/value pair in a dict
    # @param str (key)
    # @param str (val)
    # @param dict (dictio) 
    #   
    def update_key(key, val, dictio) :
        if key in dictio :
            dictio[key].append(val)
        else :
            dictio[key] = []
            dictio[key].append(val)
    
    #
    # Stores all the urls written in src/url_management/textFiles/urls_api.txt in self.urls
    #
    def get_all_urls(self) :
        with open('src/url_management/textFiles/urls_api.txt', 'r') as file :
            for line in file :
                tempo = line.split(' ')
                Request_Manager.update_key(tempo[0], tempo[1][:-1], self.__urls)

    #
    # Requests the api with all the urls stored in self.urls,
    # and stores all the api responses.text in self.data
    #
    def request_data(self) :
        for key, value in self.__urls.items() :
            for url in value :
                response = requests.get(url)
                if key not in self.data :
                    self._data[key] = []
                    self._data[key].append(json.loads(response.text))
                else :
                    self._data[key].append(json.loads(response.text))


    