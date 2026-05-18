from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

 #property e setters--------------------------------------------------------------------------------------

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

#-----------------------------------------------------------------------------------------------------------

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, idade: int):
        super().__init__(nome, celular, cpf)
        self.__idade = idade

#getter e setter, confirmação de idade do paciente
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def eh_maior_de_idade(self):
        return self.__idade >= 18



#------------------------------------------------------------------------------------------------------------

class Profissional(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro: str):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro = registro

    # Getters e Setters específicos do profissional

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    @property
    def registro(self):
        return self.__registro
    
    @registro.setter
    def registro(self, registro):
        self.__registro = registro

#------------------------------------------------------------------------------------------------------------