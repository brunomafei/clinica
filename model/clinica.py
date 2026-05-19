from abc import ABC
from datetime import date, time


class Clinica: 

    def __init__(self,
                 nome: str,
                 cidade: str,
                 descricao: str,
                 horario_abertura: time,
                 horario_fechamento: time):

        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):

        if novo_nome == "":
            raise ValueError("Nome inválido.")

        self.__nome = novo_nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, nova_cidade):

        if nova_cidade == "":
            raise ValueError("Cidade inválida.")

        self.__cidade = nova_cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario):
        self.__horario_abertura = horario

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario):
        self.__horario_fechamento = horario

    # regra do trabalho
    def horario_funcionamento(self,
                              horario_inicio,
                              horario_fim):

        return (
            self.__horario_abertura <= horario_inicio and
            horario_fim <= self.__horario_fechamento
        )

    def __str__(self):

        return (
            f"Clínica: {self.__nome} "
            f"- {self.__cidade}"
        )
