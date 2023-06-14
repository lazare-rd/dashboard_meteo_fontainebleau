import requests
from src.url_management import UrlGenerator

class DataWriter :
    
    #
    # The constructor gets all the data needed (modeles, attributs, coordinates) to build the urls
    #
    def __init__(self) :
        self.generator = UrlGenerator.UrlGenerator()
        self.modeles = self.generator.getFileLines('src/url_management/textFiles/modeles.txt')
        self.attributes = self.generator.getFileLines('src/url_management/textFiles/attributs.txt')
        self.coordo = self.generator.getCoordo()
    
    #
    # Returns all the api urls in a dict( city : [urls] ).
    # There is one url by modele
    # @return dict( str : [str] )
    #
    def build_all_api_url(self) :
        urls = {}
        for city in self.coordo.keys() :
            urls[city] = []
            for modele in self.modeles :
                url = self.generator.buildUrl(self.coordo[city][0],
                                        self.coordo[city][1],
                                        modele,
                                        self.attributes)
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
    
