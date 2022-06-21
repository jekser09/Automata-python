class Estados():

    def __init__(self):        
        self.__cadena=""
        self.__estadoActual="A"
        self.__aceptacion=False
        self.__tipoCadena=""

    def getCadena(self):
        return self.__cadena

    def setCadena(self,valor):
        self.__cadena=valor

    def getEstadoActual(self):
        return self.__estadoActual

    def setEstadoActual(self,valor):
        self.__estadoActual=valor
    
    def getAceptacion(self):
        return self.__aceptacion

    def setAceptacion(self, valor):
        self.__aceptacion=valor

    def getTipoCadena(self):
        return self.__tipoCadena

    def setTipoCadena(self,valor):
        self.__tipoCadena=valor