import sys
from conexion import Conector

class DaoCuenta(Conector):
    def __init__(self):
        super().__init__()


    def consultar2 (self, buscar2):
        result2 = False
        try:
            sql = "Select id, codigo cod, grupo gru, descripcion des, naturaleza nat, estado est From plancuenta where descripcion like '%" + \
                str(buscar2) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result2 = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta ", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result2


    def ingresar2 (self, cuen):
        correcto2= True
        try:
            sql="insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s, %s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (cuen.Codigo, cuen.Grupo, cuen.Descripcion, cuen.Naturaleza, cuen.Estado))
            self.conn.commit()
        except Exception as e:
            print("Error al Ingresar", e)
            correcto2 = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto2


    def modificar2 (self, cuen):
        correcto2 = True
        try:
            sql='Update plancuenta set Codigo = %s, Grupo = %s, Descripcion = %s, Naturaleza = %s, Estado = %s where Id = %s'
            self.conectar()
            self.conector.execute(sql, (cuen.Codigo, cuen.Grupo, cuen.Descripcion, cuen.Naturaleza, cuen.Estado, cuen.Id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto2 = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto2


    def eliminar2 (self, cuen):
        correcto2= True
        try:
            sql="Delete from plancuenta where id = %s"
            self.conectar()
            self.conector.execute(sql, int(cuen.Id))
            self.conn.commit()
        except Exception as e: 
            print("Error al eliminar", e)
            correcto2 = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto2

""" con = DaoCuenta()
cuenta = con.consultar("")
print (cuenta)
for cuen in cuenta:
    print(cuen[1])
"""