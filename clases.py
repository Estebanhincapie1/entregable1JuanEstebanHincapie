class Paciente():
    def __init__(self) -> None:
        self.__nombre = ""
        self.__cedula = 0
        self.__implantes = {}
    
    #        GETTERS
    def asignarNombre(self, nombre):
        self.__nombre = nombre.upper()
    def asignarCedula(self, cedula):
        self.__cedula = cedula
    def asignarImplantes(self, implante):
        self.__implantes[implante.verNombre()] = implante  

    #        SETTERS   
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verImplantes(self):
        for i in self.__implantes.values(): 
            print(f'{i}\n')

    def lenImplantes(self):
        return len(self.__implantes)
    
    #      Metodos asociados al diccionario contenedor de los implantes

    def eliminarImplante(self,c): 
        self.__implantes.pop(c)
        return True
    
    def modificarImplante(self,nuevoImplante):
        self.__implantes[nuevoImplante.verNombre()] = nuevoImplante

    def __str__(self) -> str:
        return f'      Nombre del paciente: {self.verNombre()}\n      Cedula: {self.verCedula()}\n      Implantes: {self.verImplantes()}'



class Marcapasos():
    def __init__(self) -> None:
        self.__nombre = 'MARCAPASO'
        self.__NumElectrodos = 0
        self.__Conexion = 0      
        self.__FrecEstimulacion = 0
        self.__fechaImplantacion = None
        self.__doctor = ''
        self.__estado = ''
    
    def asignarNumElectrodos(self, c):
        self.__NumElectrodos = c
    def asignarConexion(self, c):
        self.__Conexion = c
    def asignarFRECUENCIA(self, c):
        self.__FrecEstimulacion = c
    def asignarFechaImplantacion(self, fecha):
        self.__fechaImplantacion = fecha  
    def asignarDoctor(self, doc):
        self.__doctor = doc        
    def asignarEstado(self,e):
        self.__estado = e 
    def verNombre(self):
        return self.__nombre
    

    def __str__(self) -> str:
        return f"""      MARCAPASO:\n      Numero de electrodos: {self.__NumElectrodos}\n      Conexion: {self.__Conexion}\n      Frecuencia de Estimulacion: {self.__FrecEstimulacion}\n      Fecha de implantacion: {self.__fechaImplantacion}\n      Doctor encargado: {self.__doctor} \n      Estado del Implante: {self.__estado}"""
    
    
class StentCoronario():
    def __init__(self) -> None:
        self.__nombre  = 'STENT CORONARIO'
        self.__longitud = 0
        self.__diametro = 0
        self.__material = ""
        self.__fechaImplantacion = None
        self.__doctor = ''
        self.__estado = ''


    def asignarLongitud(self,c):
        self.__longitud = c
    def asignarDiametro(self, c):
        self.__diametro = c
    def asignarMaterial(self, c):
        self.__material = c
    def asignarFechaImplantacion(self, fecha):
        self.__fechaImplantacion = fecha  
    def asignarDoctor(self, doc):
        self.__doctor = doc
    def asignarEstado(self,e):
        self.__estado = e 
    def verNombre(self):
        return self.__nombre
    
    def __str__(self) -> str:
        return f"      STENT CORONARIO:\n      Longitud: {self.__longitud}\n      Diametro: {self.__diametro}\n      Material: {self.__material}\n      Fecha de implantacion: {self.__fechaImplantacion}\n      Doctor encargado: {self.__doctor}\n      Estado del Implante: {self.__estado}"

class ImplanteDental():
    def __init__(self) -> None:
        self.__nombre = 'IMPLANTE DENTAL'
        self.__forma = ""
        self.__sistemaFijacion = ""
        self.__material = "" 
        self.__fechaImplantacion = None
        self.__doctor = '' 
        self.__estado = ''
           

    def asignarForma(self, f):
        self.__forma = f
    def asignarSistemaFijacion(self,s):
        self.__sistemaFijacion = s
    def asignarMaterial(self, m):
        self.__material = m
    def asignarFechaImplantacion(self, fecha):
        self.__fechaImplantacion = fecha  
    def asignarDoctor(self, doc):
        self.__doctor = doc 
    def asignarEstado(self,e):
        self.__estado = e 
    def verNombre(self):
        return self.__nombre

    def __str__(self) -> str:
        return f'   {self.__nombre}\n      Forma: {self.__forma}\n      Sistema de Fijación: {self.__sistemaFijacion}\n      Material: {self.__material}\n      Fecha de Implantacion: {self.__fechaImplantacion}\n      Doctor Responsable: {self.__doctor}\n      Estado del Implante: {self.__estado}'  

class ImplanteRodilla():
    def __init__(self) -> None:
        self.__nombre = 'IMPLANTE DE RODILLA'
        self.__material =''
        self.__forma = ''
        self.__size = ''
        self.__fechaImplantacion = None
        self.__doctor = ''
        self.__estado = ''
        
    def asignarMaterial(self,c):
        self.__material = c
    def asignarForma(self, c):
        self.__forma = c
    def asignarFechaImplantacion(self, fecha):
        self.__fechaImplantacion = fecha  
    def asignarDoctor(self, doc):
        self.__doctor = doc 
    def asignarEstado(self,e):
        self.__estado = e 
    def asignarSize(self,s):
        self.__size = s
    def verNombre(self):
        return self.__nombre
    
    def __str__(self) -> str:
        return f'       {self.__nombre}\n      Material: {self.__material}\n      Forma: {self.__forma}\n      Tamaño: {self.__size}\n      Fecha de implantación: {self.__fechaImplantacion}\n      Doctor Responsable: {self.__doctor}\n      Estado del Implante: {self.__estado}'
        
class ImplanteCadera(ImplanteRodilla):
    def __init__(self) -> None:
        super().__init__()
        self.__nombre = 'IMPLANTE DE CADERA'
        
    def __str__(self) -> str:
        return super().__str__() 
    
class Sistema():
    def __init__(self) -> None:
        self.__pacientes = {}
    
    def ingresarPaciente(self, paciente):
        self.__pacientes[paciente.verCedula()] = paciente
        print('\n---------PACIENTE AGREGADO CORRECTAMENTE----------')
        return True

    def eliminarPaciente(self, cedula):
        self.__pacientes.pop(cedula)

    def modificarPaciente(self, newPac):  
        self.__pacientes[newPac.verCedula()]= newPac

    def verPaciente(self, cedula):
        return self.__pacientes[cedula]

        
    def verificarExistencia(self, cedula):
        if cedula in self.__pacientes:
            return True
        else:
            return False
