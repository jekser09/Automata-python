from Estados import *


class Automatas():

    def __init__(self):
        
        self.__estEntero=Estados()                      
        self.__estReal=Estados()
        self.__estNotC=Estados()
        self.__estCorreo=Estados()
        
    def aEntero(self,caracteres="defecto"):       
        self.__estEntero.setCadena(caracteres)       
        i=0
        error=""            
        while i<str.__len__(caracteres):
            
            if caracteres[i]=="+" and self.__estEntero.getEstadoActual()=="A":                
                self.__estEntero.setEstadoActual("B")
                self.__estEntero.setTipoCadena("Positivo")
                i=i+1
            elif caracteres[i]=="-" and self.__estEntero.getEstadoActual()=="A":
                self.__estEntero.setEstadoActual("C")
                self.__estEntero.setTipoCadena("Negativo")
                i=i+1
            elif str.isdigit(caracteres[i]) and self.__estEntero.getEstadoActual()=="A":
                self.__estEntero.setEstadoActual("D")
                self.__estEntero.setAceptacion(True)
                self.__estEntero.setTipoCadena("Sin Signo")
                i=i+1
            elif self.__estEntero.getEstadoActual()=="B":
                if str.isdigit(caracteres[i]):                    
                    self.__estEntero.setEstadoActual("D")
                    self.__estEntero.setAceptacion(True)
                    i=i+1
                else:
                    error=caracteres[i]
                    self.__estEntero.setAceptacion(False)
                    break
            elif self.__estEntero.getEstadoActual()=="C":
                if str.isdigit(caracteres[i]):
                    self.__estEntero.setEstadoActual("D")
                    self.__estEntero.setAceptacion(True)
                    i=i+1
                else:
                    error=caracteres[i]
                    self.__estEntero.setAceptacion(False)
                    break
            elif self.__estEntero.getEstadoActual()=="D":
                if str.isdigit(caracteres[i]):
                    self.__estEntero.setAceptacion(True)
                    i=i+1
                else:                    
                    error=caracteres[i]
                    self.__estEntero.setAceptacion(False)
                    break
            else:
                error=caracteres[i]
                break
        
        
        if self.__estEntero.getEstadoActual()==("D") and self.__estEntero.getAceptacion():            
            return f"La cadena ({caracteres}) "+"es de tipo: "+"Entero "+self.__estEntero.getTipoCadena()
        elif self.__estEntero.getEstadoActual()==("D") and self.__estEntero.getAceptacion()==False:
            return f"La cadena ({caracteres}) "+f"es incorrecta en: {error}"
        else:
            return f"La Cadena ({caracteres}) "+f"es incorrecta en: {error}"
        
    
    def aReales(self,caracteres):
        self.__estReal.setCadena(caracteres)
        i=0
        posError=0
        error=""
        while i<self.__estReal.getCadena().__len__():
            if self.__estReal.getCadena()[i]=="+" and self.__estReal.getEstadoActual()=="A":
                self.__estReal.setEstadoActual("B")
                self.__estReal.setTipoCadena("Positivo")
                i=i+1
            elif self.__estReal.getCadena()[i]=="-" and self.__estReal.getEstadoActual()=="A":
                self.__estReal.setEstadoActual("C")
                self.__estReal.setTipoCadena("Negativo")
                i=i+1
            elif self.__estReal.getCadena()[i].isdigit() and self.__estReal.getEstadoActual()=="A":
                self.__estReal.setEstadoActual("D")
                self.__estReal.setTipoCadena("Sin signo")
                i=i+1
            elif self.__estReal.getCadena()[i].isdigit() and self.__estReal.getEstadoActual()=="B":
                self.__estReal.setEstadoActual("D")
                i=i+1
            elif self.__estReal.getCadena()[i].isdigit() and self.__estReal.getEstadoActual()=="C":
                self.__estReal.setEstadoActual("D")
                i=i+1
            elif self.__estReal.getEstadoActual()=="D":
                if  self.__estReal.getCadena()[i].isdigit():
                    i=i+1
                elif self.__estReal.getCadena()[i]==".":
                    self.__estReal.setEstadoActual("E")
                    i=i+1                    
                else:
                    posError=i
                    break            
            elif self.__estReal.getEstadoActual()=="E" and self.__estReal.getCadena()[i].isdigit():
                self.__estReal.setEstadoActual("F")
                self.__estReal.setAceptacion(True)
                i=i+1                 
            elif self.__estReal.getCadena()[i].isdigit() and self.__estReal.getEstadoActual()=="F":
                i=i+1           
            else:    
                self.__estReal.setAceptacion(False)
                error=self.__estReal.getCadena()[i]
                break
        
        if self.__estReal.getEstadoActual()=="F" and self.__estReal.getAceptacion():
            return f"La cadena ({self.__estReal.getCadena()}) es de tipo:"+f" Real {self.__estReal.getTipoCadena()}"
        elif self.__estReal.getEstadoActual()=="F" and self.__estReal.getAceptacion()==False:
            return f"La cadena ({self.__estReal.getCadena()}) es incorrecta en: {error}"
        elif self.__estReal.getEstadoActual()=="D":          
            return f"En la cadena ({self.__estReal.getCadena()}) falta el caracter '.'"
        elif self.__estReal.getEstadoActual()=="E":
            return f"En la cadena ({self.__estReal.getCadena()}) falta un digito como minimo despues de '.'"
        else:            
            return f"La cadena ({self.__estReal.getCadena()}) es incorrecta en: {error}"
    
    def aNotC(self, caracteres):
        self.__estNotC.setCadena(caracteres)
        i=0        
        error=""        
        while i<self.__estNotC.getCadena().__len__():
            if  self.__estNotC.getEstadoActual()=="A":
                if self.__estNotC.getCadena()[i]=="+":
                    self.__estNotC.setEstadoActual("B")
                    self.__estNotC.setTipoCadena("Positivo")
                    i=i+1
                elif self.__estNotC.getCadena()[i]=="-":                    
                    self.__estNotC.setEstadoActual("C")
                    self.__estNotC.setTipoCadena("Negativo")
                    i=i+1
                elif self.__estNotC.getCadena()[i].isdigit():                    
                    self.__estNotC.setEstadoActual("D")
                    self.__estNotC.setTipoCadena("Sin signo")
                    i=i+1
                else:
                    error=self.__estNotC.getCadena()[i]
                    break
            elif self.__estNotC.getEstadoActual()=="B" and self.__estNotC.getCadena()[i].isdigit():
                self.__estNotC.setEstadoActual("D")
                i=i+1
            elif self.__estNotC.getEstadoActual()=="C" and self.__estNotC.getCadena()[i].isdigit():
                self.__estNotC.setEstadoActual("D")
                i=i+1
            elif self.__estNotC.getEstadoActual()=="D":                             
                if self.__estNotC.getCadena()[i].isdigit():                    
                    i=i+1
                elif self.__estNotC.getCadena()[i]==".":
                    self.__estNotC.setEstadoActual("E")
                    i=i+1
                else:
                    error=self.__estNotC.getCadena()[i]
                    break
            elif self.__estNotC.getEstadoActual()=="E" and self.__estNotC.getCadena()[i].isdigit():
                self.__estNotC.setEstadoActual("F")
                i=i+1
            elif self.__estNotC.getEstadoActual()=="F":
                if self.__estNotC.getCadena()[i].isdigit():
                    i=i+1
                elif self.__estNotC.getCadena()[i]=="E":
                    self.__estNotC.setEstadoActual("G")
                    i=i+1
                else:
                    error=self.__estNotC.getCadena()[i]
                    break
            elif self.__estNotC.getEstadoActual()=="G":
                if self.__estNotC.getCadena()[i]=="+":
                    self.__estNotC.setEstadoActual("H")
                    i=i+1
                elif self.__estNotC.getCadena()[i]=="-":
                    self.__estNotC.setEstadoActual("I")
                    i=i+1
                elif self.__estNotC.getCadena()[i].isdigit():
                    self.__estNotC.setEstadoActual("J")
                    self.__estNotC.setAceptacion(True)
                    i=i+1
                else:
                    error=self.__estNotC.getCadena()[i]
                    break
            elif self.__estNotC.getEstadoActual()=="H" and self.__estNotC.getCadena()[i].isdigit():
                self.__estNotC.setEstadoActual("J")
                self.__estNotC.setAceptacion(True)
                i=i+1
            elif self.__estNotC.getEstadoActual()=="I" and self.__estNotC.getCadena()[i].isdigit():
                self.__estNotC.setEstadoActual("J")
                self.__estNotC.setAceptacion(True)
                i=i+1
            elif self.__estNotC.getEstadoActual()=="J" and self.__estNotC.getCadena()[i].isdigit():
                i=i+1
            else:
                error=self.__estNotC.getCadena()[i]
                self.__estNotC.setAceptacion(False)
                break

        if self.__estNotC.getEstadoActual()=="J"  and self.__estNotC.getAceptacion():
            return f"La cadena ({self.__estNotC.getCadena()}) es de tipo:"+f" Notacion C. {self.__estNotC.getTipoCadena()}"
        elif self.__estNotC.getEstadoActual()=="J" and self.__estNotC.getAceptacion()==False:
            return f"La cadena ({self.__estNotC.getCadena()}) es incorrecta en:"+f" Notacion C. {error}"
        elif self.__estNotC.getEstadoActual()=="D":
            return f"En la cadena ({self.__estNotC.getCadena()}) falta un '.'"
        elif self.__estNotC.getEstadoActual()=="E":
            return f"En la cadena ({self.__estNotC.getCadena()}) faltan uno o mas digitos despues de '.'"
        elif self.__estNotC.getEstadoActual()=="F":
            return f"En la cadena ({self.__estNotC.getCadena()}) falta un el caracter que indica el Exponente 'E'"
        elif self.__estNotC.getEstadoActual()=="H":
            return f"En la cadena ({self.__estNotC.getCadena()}) falta uno o mas digitos despues del signo"
        elif self.__estNotC.getEstadoActual()=="I":
            return f"En la cadena ({self.__estNotC.getCadena()}) falta uno o mas digitos despues del signo"
        else:
            return f"La cadena ({self.__estNotC.getCadena()}) es incorrecta en:"+f" Notacion C. {error}"
    
    def caracter_Especial(self,caracter):
        if ord(caracter)==33:
            return True
        elif ord(caracter)==42:
            return True
        elif ord(caracter)>=35 and ord(caracter)<=38:
            return True
        elif ord(caracter)>=45 and ord(caracter)<=47:
            return True
        elif ord(caracter)==63:
            return True
        elif ord(caracter)==92:
            return True           
        elif ord(caracter)==95:
            return True        
        else:
            return False
    
    def aCorreo(self, caracteres):
        self.__estCorreo.setCadena(caracteres)
        i=0        
        error="" 
        while i<self.__estCorreo.getCadena().__len__():
            if self.__estCorreo.getEstadoActual()=="A":
                if self.__estCorreo.getCadena()[i].isalpha():
                    self.__estCorreo.setEstadoActual("B")
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("C")
                    i=i+1
                elif self.caracter_Especial(self.__estCorreo.getCadena()[i]):
                    self.__estCorreo.setEstadoActual("D")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="B":
                if self.__estCorreo.getCadena()[i].isalpha():
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("C")
                    i=i+1
                elif self.caracter_Especial(self.__estCorreo.getCadena()[i]):
                    self.__estCorreo.setEstadoActual("D")
                    i=i+1
                elif self.__estCorreo.getCadena()[i]=="@":
                    self.__estCorreo.setEstadoActual("E")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="C":
                if self.__estCorreo.getCadena()[i].isalpha():
                    self.__estCorreo.setEstadoActual("B")
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("C")
                    i=i+1
                elif self.caracter_Especial(self.__estCorreo.getCadena()[i]):
                    self.__estCorreo.setEstadoActual("D")
                    i=i+1
                elif self.__estCorreo.getCadena()[i]=="@":
                    self.__estCorreo.setEstadoActual("E")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="D":    
                if self.__estCorreo.getCadena()[i].isalpha():
                    self.__estCorreo.setEstadoActual("B")
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("C")
                    i=i+1
                elif self.caracter_Especial(self.__estCorreo.getCadena()[i]):
                    self.__estCorreo.setEstadoActual("D")
                    i=i+1
                elif self.__estCorreo.getCadena()[i]=="@":
                    self.__estCorreo.setEstadoActual("E")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="E":
                if self.__estCorreo.getCadena()[i].isalpha():
                    self.__estCorreo.setEstadoActual("F")
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("G")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="F":
                if self.__estCorreo.getCadena()[i].isalpha():
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    self.__estCorreo.setEstadoActual("G")
                    i=i+1
                elif self.__estCorreo.getCadena()[i]==".":
                    self.__estCorreo.setEstadoActual("H")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="G":
                if self.__estCorreo.getCadena()[i].isalpha():
                    self.__estCorreo.setEstadoActual("F")
                    i=i+1
                elif self.__estCorreo.getCadena()[i].isdigit():
                    i=i+1
                elif self.__estCorreo.getCadena()[i]==".":
                    self.__estCorreo.setEstadoActual("H")
                    i=i+1
                else:
                    error=self.__estCorreo.getCadena()[i]
                    break
            elif self.__estCorreo.getEstadoActual()=="H" and self.__estCorreo.getCadena()[i].isalpha():
                self.__estCorreo.setEstadoActual("I")
                self.__estCorreo.setAceptacion(True)
                i=i+1
            elif self.__estCorreo.getEstadoActual()=="I" and self.__estCorreo.getCadena()[i].isalpha():
                i=i+1
            else:
                error=self.__estCorreo.getCadena()[i]
                self.__estCorreo.setAceptacion(False)
                break
        
        if self.__estCorreo.getEstadoActual()=="I" and self.__estCorreo.getAceptacion():
            return f"La cadena {self.__estCorreo.getCadena()}: Es un correo valido"
        elif self.__estCorreo.getEstadoActual()=="I" and self.__estCorreo.getAceptacion()==False:
            return f"La cadena {self.__estCorreo.getCadena()}: despues del punto hay un error en {error}"
        elif self.__estCorreo.getEstadoActual()=="H":
            return "Faltan letras despues del '.'"
        elif self.__estCorreo.getEstadoActual()=="E":
            return "Faltan caracteres despues del '@'"
        else:
            return f"La cadena {self.__estCorreo.getCadena()}: tiene un error en {error}"


