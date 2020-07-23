class ModGrupo:
    def __init__(self, codi=0, des=''):
        self.__G_id = codi
        self.__G_descripcion = des

    @property
    def G_id(self):
        return self.__G_id

    @property
    def G_descripcion(self):
        return self.__G_descripcion