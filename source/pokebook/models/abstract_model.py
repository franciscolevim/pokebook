class AbstractModel:
    """
    Clase base para generar el modelo de la aplicación.
    """
    def fill(self, json:map):
        """
        Llena las propiedades del modelo con información de un JSON obtenido de la pokeapi.
        
        ** Este método debe ser implementado por cada modelo de forma específica.
        """
        pass


    @property
    def url(self):
        """
        URL para poder recuperar la información desde la pokeapi.
        """
        return self.__url

    @url.setter
    def url(self, url:str):        
        self.__url = url.strip() if url else ''
