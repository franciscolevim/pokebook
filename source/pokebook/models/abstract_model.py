class AbstractModel:
    """
    Clase base para generar el modelo de la aplicación.
    """


    @property
    def url(self):
        """
        URL para poder recuperar la información desde la pokeapi.
        """
        return self.__url

    @url.setter
    def url(self, url:str):        
        self.__url = url.strip() if url else ''
