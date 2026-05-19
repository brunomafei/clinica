class Pagamento(ABC):

    def __init__(self,
                 data_pagamento: date,
                 atendimento,
                 paciente,
                 valor_pago: float,
                 tipo_pagamento: str,
                 cpf_pagador=None,
                 numero_cartao=None,
                 bandeira=None):

        # regra do trabalho
        if data_pagamento > atendimento.data:

            raise ValueError(
                "Pagamento deve ser realizado "
                "até a data do atendimento."
            )

        self.__data_pagamento = data_pagamento
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago
        self.__tipo_pagamento = tipo_pagamento

        # PIX
        self.__cpf_pagador = cpf_pagador

        # CARTÃO
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, nova_data):
        self.__data_pagamento = nova_data

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, novo_atendimento):
        self.__atendimento = novo_atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor):

        if novo_valor < 0:
            raise ValueError("Valor inválido.")

        self.__valor_pago = novo_valor

    @property
    def tipo_pagamento(self):
        return self.__tipo_pagamento

    @tipo_pagamento.setter
    def tipo_pagamento(self, tipo):
        self.__tipo_pagamento = tipo

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf):
        self.__cpf_pagador = cpf

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero):
        self.__numero_cartao = numero

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, nova_bandeira):
        self.__bandeira = nova_bandeira

    def calcular_valor_restante(self):

        return (
            self.__atendimento.valor -
            self.__valor_pago
        )

    def __str__(self):

        if self.__tipo_pagamento == "PIX":

            return (
                f"Pagamento PIX - "
                f"CPF: {self.__cpf_pagador}"
            )

        elif self.__tipo_pagamento == "CARTAO":

            return (
                f"Pagamento Cartão - "
                f"Bandeira: {self.__bandeira}"
            )

        else:

            return "Pagamento em Dinheiro" # cada modalidade (como CPF no PIX ou Bandeira no Cartão).
