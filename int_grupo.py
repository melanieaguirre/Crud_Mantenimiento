from ctr_grupo import CtrGrupos
from mod_grupo import ModGrupo
#from funciones import menu 
#import os
ctr = CtrGrupos()

def insertar(rango):
    for _ in range(int(rango)):         ##corregir por la i 
        descripcion = ''
        while descripcion.strip() == '':
            descripcion = input('Ingrese Grupo: ')
            if descripcion.strip() != '' and descripcion.isalpha():
                g = ModGrupo(des= descripcion.strip()) 
                if ctr.ingresar(g):
                    print('Registro grabado correctamente')
                else:
                    print('Error al grabar registro')
            else:
                print('Ingrese un valor')        

def modificar():
    codigo = ''
    while codigo.strip() == '':
        codigo = input('Ingrese codigo: ')

    descripcion = ''
    while descripcion.strip() == '': 
        descripcion = input('Ingrese Grupo: ')
        if descripcion.strip() != '': 
            g = ModGrupo(codi= codigo, des= descripcion.strip())
            if ctr.modificar(g):
                print('Registro grabado correctamente')
            else:
                print('Error al grabar registro')
        else:
            print('Ingrese un valor')        

def eliminar():
    codigo = ''
    while codigo.strip() == '':
        codigo = input('Ingrese codigo: ')
        
    g = ModGrupo(codi= codigo)
    if ctr.eliminar(g):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar registro')

def consultar():
    buscar = input('Ingrese grupo a Consultar: ')
    g = ctr.consulta(buscar)
    print(' id Descripcion')
    for registro in g:
        print('{:3} {:6}' .format(registro[0], registro[1]))
       



