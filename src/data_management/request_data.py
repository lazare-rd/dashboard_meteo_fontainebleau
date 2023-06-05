import requests
from src.url_management import UrlGenerator

class DataRetriever :

    def get(self, api_url) :
        api_response = requests.get(api_url)
        return api_response
    
    def init(self) :
        self.generator = UrlGenerator.UrlGenerator()
        self.modeles = self.generator.getFileLines('src/url_management/modeles.txt')
        self.attributes = self.generator.getFileLines('src/url_management/attributs.txt')
        self.coordo = self.generator.getCoordo()
    
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
    
def main():
    retriever = DataRetriever()
    retriever.init()
    print(retriever.build_all_api_url())

if __name__ == '__main__':
    main()
    
