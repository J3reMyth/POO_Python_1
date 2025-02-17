#Importo la clase persona para heredar sus atributos
from .classPersona import persona

#Creo la clase persona
class clientes(persona): 
    #Agrego el constructor de la clase clientes
    def __init__(self, nombre_completo = '', cedula = '', telefono = '', email = ''): 

        #Heredo los atributos de la clase persona
        super().__init__(nombre_completo,cedula, telefono)
        self._email = email

    #Esta funcion se encarga de insertar los valores asignados en el constructor 
    def insertar_clientes(self): 
        try: 
            #Obtengo el arreglo de objetos del archivo de texto
            #Estructura de los datos almacenados en el txt: 
            #[ {cliente1}, {cliente2}, {cliente3} ... ]
            vDatos_archivo_clientes: list = self.insertar_obtener_datos_persona('./datos/clientes.txt', 'GET')

            vDiccionario_cliente = {} 
            vTelefonos = []

            #En esta variable tipo diccionario voy almacenando los valores de la clase
            vDiccionario_cliente["nombre_completo"] = self._nombre_completo
            vDiccionario_cliente["cedula"] = self._cedula
            vDiccionario_cliente["email"] = self._email

            #Recorro la lista de telefonos que se hayan agregado 
            for telefono in self._telefono: 
                vTelefonos.append(telefono)
            
            vDiccionario_cliente["telefonos"] = vTelefonos

            #Agrego a la lista de personas, el nuevo registro 
            vDatos_archivo_clientes.append(vDiccionario_cliente) 

            #Registro en el txt la lista de personas con el nuevo registro 
            return self.insertar_obtener_datos_persona('./datos/clientes.txt', 'SET', vDatos_archivo_clientes)
        except Exception as e: 
            raise Exception(f'Error en la clase classClientes: {str(e)}')

    def obtener_clientes(self): 
        try: 
            #Obtengo la lista de personas almacenadas en el txt (Devuelve una lista de objetos)
            vDatos_archivo_clientes: list = self.insertar_obtener_datos_persona('./datos/clientes.txt', 'GET')

            vCadena_Datos = '' 

            #Si existen datos, recorro cada item de la lista de personas 
            if len(vDatos_archivo_clientes) > 0: 
                vCadena_Datos = '\n\n-----------------CLIENTES-----------------\n\n'

                #Recorro cada item de la lista de personas 
                for i, cliente in enumerate(vDatos_archivo_clientes): 
                    vCadena_Datos += f'------------Cliente #{i+1}------------\n'
                    vCadena_Datos += f'Cedula: {cliente["cedula"]} \n'
                    vCadena_Datos += f'Nombre Completo: {cliente["nombre_completo"]} \n'
                    vCadena_Datos += f'Email: {cliente["email"]} \n'
                    vCadena_Datos += f'Telefonos: \n' 

                    #Recorro los telefonos que tiene la persona  
                    for telefono in cliente["telefonos"]: 
                        vCadena_Datos += f'\t {telefono}\n' 
                    vCadena_Datos += '\n'
                    
            else: 
                #De no existir datos solo imprimirá el mensaje de no existen datos
                vCadena_Datos = '\n------No existen datos de clientes------\n\n'
                
            return vCadena_Datos

        except Exception as e: 
            raise Exception(f'Error en la clase classClientes: {str(e)}')