from dao_grupo import DaoGrupo
from mod_grupo import ModGrupo
#from mod_cuenta import ModCuenta
class CtrGrupos:
    def __init__(self, grup=None):
        self.grupo = grup
    
    def consulta(self, buscar):
        objDao= DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, grup):
        objDao= DaoGrupo()
        return objDao.ingresar(grup)
    
    def modificar(self, grup):
        objDao= DaoGrupo()
        return objDao.modificar(grup)

    def eliminar(self, grup):
        objDao= DaoGrupo()
        return objDao.eliminar(grup)

"""grup = ModGrupo(0, 'Activo') 
ctr = CtrGrupos()
ctr.ingresar(grup)
cgrupo = ctr.consulta("")
print(cgrupo)
for grup in cgrupo:
    print(grup[0], grup[1])
    """