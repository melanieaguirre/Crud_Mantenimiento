class ModCuenta:
    def __init__(self, clv=0, cod=0, gr=0, descp='', nat= '', estado=0):
        self.__Id = clv
        self.__Codigo = cod
        self.__Grupo = gr
        self.Descripcion = descp
        self.Naturaleza = nat
        self.Estado = estado
    
    @property
    def Id(self):
        return self.__Id

    @property
    def Codigo(self):
        return self.__Codigo

    @property
    def Grupo(self):
        return self.__Grupo