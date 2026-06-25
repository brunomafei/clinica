from model.pessoa import Profissional


class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional_responsavel: Profissional, id_procedimento: int):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional_responsavel = profissional_responsavel
        self.__id_procedimento = id_procedimento

# getters e setters para os atributos do procedimento---------------------------------------------------------------------
    @property
    def id_procedimento(self):
        return self.__id_procedimento

    @id_procedimento.setter
    def id_procedimento(self, id_procedimento):
        self.__id_procedimento = id_procedimento

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo):
        self.__custo = custo

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel

    @profissional_responsavel.setter
    def profissional_responsavel(self, profissional_responsavel):
        self.__profissional_responsavel = profissional_responsavel
