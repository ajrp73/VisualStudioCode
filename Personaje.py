class Personaje:
    __slots__ = ['__nombre', '__altura', '__peso']
    
    def __init__(self, nombre, altura, peso):
        self.__nombre= nombre
        self.__altura= altura
        self.__peso= peso
        
        
    def getNombre(self):
        return self.__nombre

    def getAltura(self):
        return self.__altura
        
    def getPeso(self):
        return self.__peso

    def setNombre(self, nombre):
        self.__nombre= nombre

    def setAltura(self, altura):
        self.__altura= altura        
    
    def setPeso(self, peso):
        self.__peso= peso
    
    def toString(self):
        cad="Personaje[" + self.getNombre() + ", "
        cad+=str(self.__altura) + ", " 
        cad+=str(self.__peso) + "]"
        return cad
        
   # def reset(): #Pone el nombre a cadena vacía y peso y altura a valor 0


soldado1= Personaje("A", 1.0, 2.0)
soldado2= Personaje("B", 3.0, 4.0)


print("s1:",soldado1.toString())
print("s2:",soldado2.toString())

soldado1.setNombre("s1")
#cuatriplicar altura de soldado1 sin saber que es 1.0
#con var. auxiliar s1a
s1a=soldado1.getAltura()
s1a= 4*s1a
soldado1.setAltura(s1a)

#sin var. auxiliar 
soldado1.setAltura(4*soldado1.getAltura())
print("s1:",soldado1.toString())

print("soldado")
#Principio de ocultación 
try:
    soldado1.__altura=-1  #No tiene efecto pero no produce error
except Exception:
    print("Error. El atributo es privado.")

try:
    soldado1.altura=-2    #Se permite la incorporación dinámica de atributos in el uso de __slots__
    print(f"s1: {soldado1.altura}")
except Exception:
    print("Error. El atributo altura no se puede incorporar.")
    
soldado1.setAltura(4*soldado1.getAltura())
print("s1:",soldado1.toString())
