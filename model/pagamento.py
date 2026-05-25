from abc import ABC, abstractmethod
from datetime import date

# Superclasse Abstrata


class Pagamento(ABC):
    def __init__(self, data: date, valor_pago: float, atendimento=None):
        if atendimento and data > atendimento.data:
            raise ValueError(
                "Pagamento deve ser realizado até a data do atendimento.")

        self.__data = data
        self.__valor_pago = valor_pago
        self.__atendimento = atendimento

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Valor inválido.")
        self.__valor_pago = novo_valor

    def calcular_valor_restante(self):
        if self.__atendimento:
            return self.__atendimento.valor_total - self.__valor_pago
        return 0

    @abstractmethod
    def __str__(self):
        pass


# Subclasse: Pagamento via PIX
class Pagamento_pix(Pagamento):
    def __init__(self, data: date, valor_pago: float, chave_pix: str, atendimento=None):
        super().__init__(data, valor_pago, atendimento)
        self.__chave_pix = chave_pix

    @property
    def chave_pix(self):
        return self.__chave_pix

    @chave_pix.setter
    def chave_pix(self, nova_chave):
        self.__chave_pix = nova_chave

    def __str__(self):
        return f"Pagamento PIX - Chave: {self.__chave_pix}"


# Subclasse: Pagamento via Cartão
class Pagamento_cartao(Pagamento):
    def __init__(self, data: date, valor_pago: float, numero_cartao: str, bandeira: str, atendimento=None):
        super().__init__(data, valor_pago, atendimento)
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


# Subclasse: Pagamento via Cédula (Dinheiro)
class Pagamento_cedula(Pagamento):
    def __init__(self, data: date, valor_pago: float, atendimento=None):
        super().__init__(data, valor_pago, atendimento)

    def __str__(self):
        return "Pagamento em Cédula (Dinheiro)"
