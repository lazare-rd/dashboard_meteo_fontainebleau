import requests
from src.url_management import UrlGenerator

class DataWriter :
    
    #
    # The constructor gets all the data needed (modeles, attributs, coordinates) to build the urls
    #
    def __init__(self) :
        DataWriter.generator = UrlGenerator.UrlGenerator()
        DataWriter.modeles = self.generator.getFileLines('src/url_management/textFiles/modeles.txt')
        DataWriter.attributes_ecmwf = self.generator.getFileLines('src/url_management/textFiles/attributs/attributs_ecmwf.txt')
        DataWriter.attributes_forecast = self.generator.getFileLines('src/url_management/textFiles/attributs/attributs_forecast.txt')
        DataWriter.attributes_mf_dwd = self.generator.getFileLines('src/url_management/textFiles/attributs/attributs_mf_dwd.txt')
        DataWriter.coordo = self.generator.getCoordo()
    
    #
    # Custom switch/case function
    # @param str (modele)
    # @param str (city)
    # @return str (url)
    #
    def switch(modele, city):
        if modele == 'forecast':
            url = DataWriter.generator.buildUrl(DataWriter.coordo[city][0],
                                        DataWriter.coordo[city][1],
                                        modele,
                                        DataWriter.attributes_forecast)
            return url
        elif modele == 'dwd-icon' or modele == 'meteofrance' :
            url = DataWriter.generator.buildUrl(DataWriter.coordo[city][0],
                                        DataWriter.coordo[city][1],
                                        modele,
                                        DataWriter.attributes_mf_dwd)
            return url
        elif modele == 'ecmwf' : 
            url = DataWriter.generator.buildUrl(DataWriter.coordo[city][0],
                                        DataWriter.coordo[city][1],
                                        modele,
                                        DataWriter.attributes_ecmwf)
            return url
        
    #
    # Returns all the api urls in a dict( city : [urls] ).
    # There is one url by modele
    # @return dict( str : [str] )
    #
    def build_all_api_url(self) :
        urls = {}
        for city in DataWriter.coordo.keys() :
            urls[city] = []
            for modele in DataWriter.modeles :
                url = DataWriter.switch(modele, city)
                urls[city].append(url)
        return urls


    #
    # Writes all the api_urls in src/url_management/textFiles/urls_api.txt
    # @param dict( str : [str] ) (keys are cities and values are list of urls)
    #
    def write_all_api_urls(self, api_urls) :
        with open('src/url_management/textFiles/urls_api.txt','w') as file :
            for city in api_urls.keys():
                for url in api_urls[city]:
                    file.write(f'{city} {url}\n')
    
def main():
    writer = DataWriter()
    urls_apis = writer.build_all_api_url()
    writer.write_all_api_urls(urls_apis)

if __name__ == '__main__':
    main()
    
