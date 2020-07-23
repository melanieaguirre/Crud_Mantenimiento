from int_grupo import insertar, modificar, eliminar, consultar
from int_cuenta import inser_cuen, modi_cuen, elim_cuen, consu_cuen
from funciones import menu 
import os


def grupo():
    opc = ''
    while True:
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'], 
            'Menu Grupo'))   
        if opc == '0':
            print('\n<<<Insertar datos>>> ')
            valor = input('Ingrese cantidad de datos a Ingresar: ')
            insertar(valor)
            input('Presione una tecla para continuar')
        elif opc == '1':
            print('\n<<<Modificar datos>>> ')
            modificar()
            input('Presione una tecla para continuar')
        elif opc == '2':
            print('\n<<<Eliminar datos>>> ')
            eliminar()
            input('Presione una tecla para continuar')
        elif opc == '3':
            print('\n<<<Consultar datos>>> ')
            consultar()
            input('Presione una tecla para continuar')
        elif opc == '4':
            #print('<<<Gracias por usar el sistema>>>')
            #input('Presione una tecla para continuar')

            break
        elif opc != '4':
            print('Seleccione una opcion correcta')
            input('Presione una tecla para continuar')
            os.system('cls')


def cuenta():
    opc = ''
    while True:
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'], 
            'Menu Cuenta'))
        if opc == '0':
            print('\n<<<Insertar datos>>> ')
            valor2 = input('Ingrese cantidad de datos a Ingresar')
            inser_cuen(valor2)
            input('Presione una tecla para continuar')
        elif opc == '1':
            print('\n<<<Modificar datos>>> ')
            modi_cuen()
            input('Presione una tecla para continuar')
        elif opc == '2':
            print('\n<<<Eliminar datos>>> ')
            elim_cuen()
            input('Presione una tecla para continuar')
        elif opc == '3':
            print('\n<<<Consultar datos>>> ')
            consu_cuen()
            input('Presione una tecla para continuar')
        elif opc == '4':
            #print('<<<Gracias por usar el sistema>>>')
           # input('Presione una tecla para continuar')
            break
        elif opc != '4':
            print('Seleccione una opcion correcta')
            input('Presione una tecla para continuar')
            os.system('cls')


def ejecutar_principal():
    opc = ''
    while True:
        opc = str(menu(
            ['Grupos de Cuentas', 'Plan de Cuenta', 'Salir'], 
            'Menu Principal'))
        if opc == '0':
            grupo()
        elif opc == '1':
            cuenta()
        elif opc == '2':
            print('<<<Gracias por usar el sistema>>>')
            input('Presione una tecla para continuar')
            exit()
            break
        elif opc != '2':
            print('Seleccione una opcion correcta')
            input('Presione una tecla para continuar')
            os.system('cls')

ejecutar_principal()