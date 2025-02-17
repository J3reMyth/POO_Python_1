
import os 
import json #CON ESTA LIBRERIA PUEDO UTILIZAR LOS DATOS TIPO JSON COMO DICCIONARIOS

#------------------------------------------INICIO CLASE PERSONA------------------------------------------
class persona: 

    #CREO CONSTRUCTOR QUE ASIGNARA VALORES A LOS ATRIBUTOS
    def __init__(self, nombre_completo = '', cedula = '', telefono = ''):
        self._nombre_completo = nombre_completo
        self._cedula = cedula
        self._telefono = telefono 

    #Esta funcion se encargará de manejar el archivo de preferencia
    def insertar_obtener_datos_persona(self, ruta_archivo, tipo_proceso, datos =''):
        try:
            vFile = None
            vResults = ""

            #Si no existe el archivo lo creará y meterá un arreglo vacío
            if not os.path.exists(ruta_archivo): 
                vFile = open(ruta_archivo, 'w') 
                vFile.write(json.dumps([]))
                vFile.close()
                
            #CON GET OBTENGO LOS DATOS Y LOS DEVUELVO 
            if tipo_proceso == 'GET': 

                vFile = open(ruta_archivo, 'r') 
                vResults = json.loads(vFile.read())

                vFile.close()

            #CON SET METO DATOS DENTRO DEL ARCHIVO DE PREFERENCIA
            elif tipo_proceso == 'SET': 
                vFile = open(ruta_archivo, 'w')
                vFile.write(json.dumps(datos))
                vResults= True
                vFile.close()

            return vResults
        except Exception as e: 
            raise Exception(f'Error en la clase persona: {str(e)}')