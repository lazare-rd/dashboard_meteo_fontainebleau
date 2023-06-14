import requests
import pandas as pd

class Requete : 

    #
    # Constructor
    # self.urls : dict( city : [urls] ) (urls as str)
    # self.data : dict( city : [json] ) (json as str)
    #
    def __init__(self) :
        self.urls = {}
        self.data = {}

    #
    # Checks is a key is already in a dict
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
        with open('src/url_management/textFiles/urls_api.txt', 'w') as file :
            for line in file :
                tempo = line.split(' ')
                Requete.update_key(tempo[0], tempo[1], self.urls)

    #
    # Requests the api with all the urls stored in self.urls,
    # and stores all the api responses.text in self.data
    #
    def request_data(self) :
        for key, value in self.urls.items() :
            for url in value :
                response = requests.get(url)
                if key not in self.data :
                    self.data[key] = []
                    self.data[key].append(response.text)
                else :
                    self.data[key].append(response.text)


def main() :
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=48.44&longitude=2.60&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation_probability,precipitation,cloudcover,windspeed_10m,winddirection_10m')
    print(response.text)

if __name__ == '__main__':
    main()
    