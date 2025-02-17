#Importo la clase persona para heredar sus atributos
from .classPersona import persona

class empleados(persona): 
    #Agrego el constructor de la clase clientes
    def __init__(self, nombre_completo = '', cedula = '', telefono = '', direccion = ''): 
        #Heredo los atributos de la clase persona
        super().__init__(nombre_completo, cedula, telefono)
        self._direccion = direccion

    def insertar_empleados(self): 
        try: 
            #Obtengo el arreglo de objetos del archivo de texto
            #Estructura de los datos almacenados en el txt: 
            #[ {cliente1}, {cliente2}, {cliente3} ... ]
            vDatos_archivo_empleados: list = self.insertar_obtener_datos_persona('./datos/empleados.txt', 'GET')
            vDiccionario_empleado = {} 
            vTelefonos = []

            #En esta variable tipo diccionario voy almacenando los valores de la clase
            vDiccionario_empleado["nombre_completo"] = self._nombre_completo
            vDiccionario_empleado["cedula"] = self._cedula
            vDiccionario_empleado["direccion"] = self._direccion

            for telefono in self._telefono: 
                vTelefonos.append(telefono)
                
            vDiccionario_empleado["telefonos"] = vTelefonos


            #Agrego a la lista de personas, el nuevo registro 
            vDatos_archivo_empleados.append(vDiccionario_empleado) 

            #Registro en el txt la lista de personas con el nuevo registro 
            return self.insertar_obtener_datos_persona('./datos/empleados.txt', 'SET', vDatos_archivo_empleados)
        except Exception as e: 
            raise Exception(f'Error en la clase classEmpleados: {str(e)}')
        

    #Esta funcion se encarga de imprimir los datos almacenados en el txt 
    def obtener_empleados(self): 
        try: 
            #Obtengo la lista de personas almacenadas en el txt (Devuelve una lista de objetos)
            vDatos_archivo_empleados: list = self.insertar_obtener_datos_persona('./datos/empleados.txt', 'GET')

            vCadena_Datos = '' 

            #Si existen datos, recorro cada item de la lista de personas 
            if len(vDatos_archivo_empleados) > 0: 
                vCadena_Datos = '\n\n-----------------EMPLEADOS-----------------\n\n' 

                #Recorro cada item de la lista de personas 
                for i, empleado in enumerate(vDatos_archivo_empleados):  #Enumerate me permite saber el indice de la lista y el item que contiene 
                    
                    #Ingreso los valores a la variable vCadena_Datos
                    vCadena_Datos += f'------------EMPLEADO #{i+1}------------\n'
                    vCadena_Datos += f'Cedula: {empleado["cedula"]} \n'
                    vCadena_Datos += f'Nombre Completo: {empleado["nombre_completo"]} \n'
                    vCadena_Datos += f'Direccion: {empleado["direccion"]} \n'
                    vCadena_Datos += f'Telefonos: \n' 

                    #Recorro los telefonos que tiene la persona  
                    for telefono in empleado["telefonos"]: 
                        vCadena_Datos += f'\t {telefono}\n' 
                    vCadena_Datos += '\n'

            else: 
                #De no existir datos solo imprimirá el mensaje de no existen datos
                vCadena_Datos = '\n------No existen datos de empleados------\n\n'

            return vCadena_Datos

        except Exception as e: 
            raise Exception(f'Error en la clase classempleados: {str(e)}')