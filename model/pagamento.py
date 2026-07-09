import random
from abc import ABC, abstractmethod
from datetime import date

class Pagamento(ABC):
    def __init__(self, data: date, valor: float, atendimento=None, id_pagamento=None):
        if atendimento and data > atendimento.data:
            raise ValueError(
                "Pagamento deve ser realizado até a data do atendimento.")

        # CORREÇÃO AQUI: Forçando o ID a ser sempre uma String (texto)
        self.__id = str(id_pagamento) if id_pagamento else str(random.randint(1000, 9999))
        
        self.__data = data
        self.__valor = valor
        self.__atendimento = atendimento

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Valor inválido.")
        self.__valor = novo_valor

    def calcular_valor_restante(self):
        if self.__atendimento:
            return self.__atendimento.valor_total - self.__valor
        return 0

    @abstractmethod
    def __str__(self):
        pass


class PagamentoPix(Pagamento):
    def __init__(self, data: date, valor: float, chave_pix: str, atendimento=None):
        super().__init__(data, valor, atendimento)
        self.__chave_pix = chave_pix

    @property
    def chave_pix(self):
        return self.__chave_pix

    @chave_pix.setter
    def chave_pix(self, nova_chave):
        self.__chave_pix = nova_chave

    def __str__(self):
        return f"Pagamento PIX - Chave: {self.__chave_pix}"


class PagamentoCartao(Pagamento):
    def __init__(self, data: date, valor: float, numero_cartao: str, bandeira: str, atendimento=None):
        super().__init__(data, valor, atendimento)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    def __str__(self):
        return f"Pagamento Cartão - Bandeira: {self.__bandeira}"


class PagamentoCedula(Pagamento):
    def __init__(self, data: date, valor: float, atendimento=None):
        super().__init__(data, valor, atendimento)

    def __str__(self):
        return "Pagamento em Cédula (Dinheiro)"