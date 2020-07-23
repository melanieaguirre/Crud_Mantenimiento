import sys
from conexion import Conector


class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()
    
    def consultar (self, buscar):
        result = False
        try:
            sql="Select G_id, G_descripcion des  From grupo where G_descripcion like '%" + \
                str(buscar) + "%' order by G_id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta ", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
    
    def ingresar (self, grup):
        correcto= True
        try:
            sql="insert into grupo (G_descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql, (grup.G_descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error al crear nuevo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
    
    def modificar (self, grup):
        correcto = True
        try:
            sql='Update grupo set G_descripcion = %s where G_id = %s'
            self.conectar()
            self.conector.execute(sql, ( grup.G_descripcion, grup.G_id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
            return correcto
    
    def eliminar (self, grup):
        correcto= True
        try:
            sql="Delete from grupo where G_id = %s"
            self.conectar()
            self.conector.execute(sql, (grup.G_id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

   

"""con = DaoGrupo()
cgrupo = con.consultar("")
print (cgrupo)
for grup in cgrupo:
    print(grup[1])
    """