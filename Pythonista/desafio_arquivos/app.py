class metodo():
    def metodo_instancia(self):
        return('retornando instancia', self)  
    
    @classmethod
    def metodo_classe(cls):
        return('retornando classe', cls)
    
    @staticmethod
    def metodo_estatico():
        return("retornando estatico")