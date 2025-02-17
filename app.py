from modulos import modClientes
from modulos import modEmpleados

def menu_main(): 
    vOpcion = '0' 

    vMenu = '\n\n\n**************LIBRERIA PATITO**************\n'
    vMenu += '\n---------------MENU PRINCIPAL---------------\n'
    vMenu += 'Seleccione la opcion de preferencia \n'
    vMenu += '1. Modulo Clientes \n'
    vMenu += '2. Modulo Empleados \n' 
    vMenu += '3. Salir \n'  
    vMenu += 'Opcion: '

    #ESTE SERA EL MENU DE LA APP PRINCIPAL
    while vOpcion != '3': 
        vOpcion = input(vMenu) 
        
        if vOpcion == '1': 
            modClientes.menu_clientes() 
        elif vOpcion == '2': 
            modEmpleados.menu_empleados()
        elif vOpcion != '3': 
            print('Opcion no valida \n')
    
    exit()

menu_main()