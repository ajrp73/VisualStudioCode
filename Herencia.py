class Persona:
    __slots__ = ['__nombre', '__edad']
    
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self.__edad= edad


    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad
        
    def setNombre(self, nombre):
        self.__nombre= nombre

    def setEdad(self, edad):
        self.__edad= edad

    def toString(self):
        cad="Persona[" + self.getNombre() + ", "
        cad+=str(self.getEdad()) + "]"
        return cad

class Empleado(Persona):
    __slots__ = ['__sueldo']
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo=sueldo
        

    def getSueldo(self):
        return self.__sueldo
       
    def setSueldo(self, sueldo):
        self.__sueldo= sueldo

    def toString(self):
        cad="Empleado[" + self.getNombre() + ", "
        cad+=str(self.getEdad()) + ", "
        cad+=str(self.getSueldo()) + "]"
        return cad

class Cliente(Persona):
    __slots__ = ['__saldo']
    
    def __init__(self, nombre, edad, saldo):
        super().__init__(nombre, edad)
        self.__saldo=saldo
        

    def getSaldo(self):
        return self.__saldo
       
    def setSaldo(self, saldo):
        self.__saldo= saldo

    def toString(self):
        cad="Cliente[" + self.getNombre() + ", "
        cad+=str(self.getEdad()) + ", "
        cad+=str(self.getSaldo()) + "]"
        return cad


p1=Persona("P1", 19)
p2=Persona("P2", 20)

e1=Empleado("E1", 21, 1000)
e2=Empleado("E2", 22, 2000)

c1=Cliente("C1", 23, 300)
c2=Cliente("C2", 24, 400)

agenda= [p1, p2, e1, e2, c1, c2]

i=0
for p in agenda:
    print(f"persona {i}: {p.toString()}")
    i+=1


