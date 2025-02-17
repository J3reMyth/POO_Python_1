#IMPORTO LA CLASE EMPLEADOS
from clases.classEmpleados import empleados

def solicitar_datos_empleado(): 
    try: 
        #SOLICITO LOS DATOS PARA POSTERIORMENTE INSERTARLOS EN EL ARCHIVO TXT
        vNombre_completo = str(input('Ingrese el nombre completo del empleado: '))
        vCedula = str(input('Ingrese la cedula del empleado: ')) 
        vDireccion = str(input('Ingrese la direccion del empleado: ')) 
        vTelefono = [] 
        vAgregar_Telefono = 'S'

        #PIDO LOS TELEFONOS n CANTIDAD DE VECES HASTA QUE EL USUARIO DECIDA 
        while  vAgregar_Telefono == 'S': 
            vTelefono.append(input('Ingrese un numero de telefono del empleado: ')) 

            #Capitalize devuelve todo en mayusculas en caso de agregar un dato en minuscula
            vAgregar_Telefono = input('Desea agregar otro numero de telefono? (S / N): ').capitalize()

        #AGREGO LOS DATOS EN LA CLASE EMPLEADO 
        vClase_empleados = empleados(vNombre_completo, vCedula, vTelefono, vDireccion)

        #PROCEDO A INSERTAR LOS DATOS
        if vClase_empleados.insertar_empleados(): 
            print("\n*****EMPLEADO AGREGADO EXITOSAMENTE*****\n")
        else: 
            print('\n*****ERROR AL INSERTAR UN NUEVO EMPLEADO*****\n')
            
    except Exception as e: 
        raise Exception(f'Error al solicitar datos del empleado: {str(e)}')    

def imprimir_empleados(): 
    #INSTANCIO LA CLASE EMPLEADO
    vClase_empleados = empleados() 

    #IMPRIMO LOS RESULTADOS DEVUELTOS DE LA FUNCION 
    print(vClase_empleados.obtener_empleados()) 


def menu_empleados(): 
    vOpcion = '' 

    vMenu = '\n\n\n---------------MODULO EMPLEADOS---------------\n'
    vMenu += 'Seleccione la opcion de preferencia \n'
    vMenu += '1. Agregar empleado \n'
    vMenu += '2. Ver empleados \n' 
    vMenu += '3. Salir \n'  
    vMenu += 'Opcion: '

    #ESTE SERA EL MENU DEL MODULO DE EMPLEADO
    while vOpcion != '3': 
        vOpcion = input(vMenu) 
        
        if vOpcion == '1': 
            solicitar_datos_empleado() 
        elif vOpcion == '2': 
            imprimir_empleados() 
        elif vOpcion != '3': 
            print('\nOpcion no valida \n')
            