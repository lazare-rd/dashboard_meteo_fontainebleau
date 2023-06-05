class UrlGenerator :

    #
    # Returns the coordinates with the following structure, (city, [latitude, longitude])
    # @return : dict(str, list[str]) 
    # 
    def getCoordo(self) : 
        coordo = {}
        with open('src/url_management/coordo.txt', 'r') as file :
            for line in file :
                tempo = line.split('/')
                coordo[tempo[2][:-1]] = tempo[0:2]
        return coordo
    
    #
    # Returns the content of a textFile, line per line
    # @param : str (file path)
    # @return : list
    #
    def getFileLines(self, filePath) :
        fileLines = []
        with open(filePath, 'r') as file :
            for line in file :
                fileLines.append(line[:-1])
        return fileLines
    
    #
    # Provided with : 
    # - coordinates
    # - modele
    # - attributes
    # will build the correct url to request the data to : https://open-meteo.com
    ##########################
    # @param : str (latitude)
    # @param : str (longitude)
    # @param : str (modele)
    # @param : list[str] (attributes)
    # @return : str (url)
    #
    def buildUrl(self, lat, long, modele, attributes) : 
        attributesAsStr = ','.join([attr for attr in attributes])
        url = f"https://api.open-meteo.com/v1/{modele}?latitude={lat}&longitude={long}&hourly={attributesAsStr}"
        return url
    

    