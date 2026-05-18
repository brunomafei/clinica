#   Além disso, deve ser possível registrar procedimentos ou serviços realizados durante o atendimento.
#   Cada procedimento deve conter: descrição, custo, e profissional responsável.
from pessoa import Profissional

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional_responsavel: Profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional_responsavel = profissional_responsavel

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
    
    