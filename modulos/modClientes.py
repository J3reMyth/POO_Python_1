#IMPORTO LA CLASE CLIENTES
from clases.classClientes import clientes

def solicitar_datos_cliente(): 
    try: 
        #SOLICITO LOS DATOS PARA POSTERIORMENTE INSERTARLOS EN EL ARCHIVO TXT
        vNombre_completo = str(input('Ingrese el nombre completo del cliente: '))
        vCedula = str(input('Ingrese la cedula del cliente: ')) 
        vEmail = str(input('Ingrese el correo electronico del cliente: ')) 
        vTelefono = [] 
        vAgregar_Telefono = 'S'

        #PIDO LOS TELEFONOS n CANTIDAD DE VECES HASTA QUE EL USUARIO DECIDA 
        while  vAgregar_Telefono == 'S': 
            vTelefono.append(input('Ingrese un numero de telefono del cliente: ')) 

            #Capitalize devuelve todo en mayusculas en caso de agregar un dato en minuscula
            vAgregar_Telefono = input('Desea agregar otro numero de telefono? (S / N): ').capitalize()

        #AGREGO LOS DATOS EN LA CLASE CLIENTES 
        vClase_Clientes = clientes(vNombre_completo, vCedula, vTelefono, vEmail) 

        #PROCEDO A INSERTAR LOS DATOS, SI RETORNA TRUE ENTONCES SE INSERTO EXITOSAMENTE
        if vClase_Clientes.insertar_clientes(): 
            print("\n*****CLIENTE AGREGADO EXITOSAMENTE*****\n")
        else: 
            print('\n*****ERROR AL INSERTAR UN NUEVO CLIENTE*****\n')
    except Exception as e: 
        raise Exception(f'Error al solicitar datos del cliente: {str(e)}')
    

def imprimir_clientes(): 
    #INSTANCIO LA CLASE CLIENTES
    vClase_Clientes = clientes() 

    #IMPRIMO LOS RESULTADOS DEVUELTOS DE LA FUNCION 
    print(vClase_Clientes.obtener_clientes()) 


def menu_clientes(): 
    vOpcion = '' 

    vMenu = '\n\n\n---------------MODULO CLIENTES---------------\n'
    vMenu += 'Seleccione la opcion de preferencia \n'
    vMenu += '1. Agregar cliente \n'
    vMenu += '2. Ver clientes \n' 
    vMenu += '3. Salir \n'  
    vMenu += 'Opcion: '

    #ESTE SERA EL MENU DEL MODULO DE CLIENTES
    while vOpcion != '3': 
        vOpcion = input(vMenu) 
        
        if vOpcion == '1': 
            solicitar_datos_cliente() 
        elif vOpcion == '2': 
            imprimir_clientes() 
        elif vOpcion != '3': 
            print('\nOpcion no valida \n')
