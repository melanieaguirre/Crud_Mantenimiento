from ctr_cuenta import CtrCuenta
from mod_cuenta import ModCuenta
#from funciones import menu 
#import os

ctr2 = CtrCuenta()

def inser_cuen(rango):
    for _ in range(int(rango)):         ##corregir por la i 
        codigo2 = ''
        while codigo2.strip() == '':
            codigo2 = input('Ingrese codigo: ')
        grupo = ''
        while grupo.strip() == '':
            grupo = input('Ingrese grupo: ')    
        descripcion = ''
        while descripcion.strip() == '':
            descripcion = input('Ingrese descripcion: ')  
        naturaleza = ''
        while naturaleza.strip() == '':
            naturaleza = input('Ingrese la naturaleza (A o D): ')
            if naturaleza == 'A' or naturaleza== 'D':
                estado = ''
                while estado.strip() == '':
                    estado= input('Ingrese el estado (True o False): ')
                    if estado == 'True' or estado == 'true' or estado == 'False' or estado == 'false':
                        if estado == 'True' or estado == 'true':
                            esta = 1
                        else:
                            esta = 0
                        c = ModCuenta( cod= codigo2, gr= grupo, descp= descripcion.strip(), nat= naturaleza.strip(), estado=esta)
                        if ctr2.ingresar2(c):
                            print('Registro grabado correctamente')
                        else:
                            esta = ''
                            print('Error al grabar registro')
                    else:
                        estado = ''
                        print('El dato que ingreso no es el Correcto')
            else:
                naturaleza = ''
                print('Ingrese A o D')

def modi_cuen(): #modificador de Cuenta 
    idc = ''
    while idc.strip() == '':
        idc = input('Ingrese idc: ')
    grupo = ''
    codigo2 = ''
    while codigo2.strip() == '':
        codigo2 = input('Ingrese codigo: ')
    grupo = ''
    while grupo.strip() == '':
        grupo = input('Ingrese grupo: ')    
    descripcion = ''
    while descripcion.strip() == '':
        descripcion = input('Ingrese descripcion: ')  
    naturaleza = ''
    while naturaleza.strip() == '':
        naturaleza = input('Ingrese la naturaleza (A o D): ')
        if naturaleza == 'A' or naturaleza== 'D':
            estado = ''
            while estado.strip() == '':
                estado= input('Ingrese el estado (True o False): ')
                if estado == 'True' or estado == 'true' or estado == 'False' or estado == 'false':
                    if estado == 'True' or estado == 'true':
                        esta = 1
                    else:
                        esta = 0
                    c = ModCuenta(clv=idc ,cod= codigo2, gr= grupo, descp= descripcion.strip(), nat= naturaleza.strip(), estado=esta)
                    if ctr2.modificar2(c):
                        print('Registro Modificado correctamente')
                    else:
                        esta = ''
                        print('Error al Modificado registro')
                else:
                    estado = ''
                    print('El dato que ingreso no es el Correcto')
        else:
            naturaleza = ''
            print('Ingrese A o D')

def elim_cuen(): #Eliminar de cuenta
    idc = input('Ingrese codigo: ')
    c = ModCuenta(clv= idc)
    if ctr2.eliminar2(c):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar registro')

def consu_cuen():
    buscar2 = input('Ingrese cuenta a buscar: ')
    c = ctr2.consulta2(buscar2)
    print('Id Codigo  Grupo  Descripcion  Naturaleza Estado')
    for registro2 in c:
        print('{:2} {:3} {:7} {:3} {:6} {:7}' .format(registro2[0], registro2[1], registro2[2], registro2[3],registro2[4], int.from_bytes(registro2[5],byteorder='big')))


