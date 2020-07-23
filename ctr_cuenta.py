from dao_cuenta import DaoCuenta
from mod_cuenta import ModCuenta

class CtrCuenta:
    def __init__(self, cuen=None):
        self.plancuenta = cuen

    def consulta2(self, buscar2):
        objDao= DaoCuenta()
        return objDao.consultar2(buscar2)

    def ingresar2(self, cuen):
        objDao= DaoCuenta()
        return objDao.ingresar2(cuen)
    
    def modificar2(self, cuen):
        objDao= DaoCuenta()
        return objDao.modificar2(cuen)

    def eliminar2(self, cuen):
        objDao= DaoCuenta()
        return objDao.eliminar2(cuen)