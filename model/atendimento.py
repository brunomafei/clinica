import random
from datetime import date, time

class Atendimento:
    def __init__(self,
                 clinica,
                 paciente,
                 profissional,
                 data: date,
                 horario_inicio: time,
                 horario_fim: time,
                 tipo: str,
                 valor_total: float,
                 id_atendimento=None):

        # Regras de Negócio
        if not paciente.eh_maior_de_idade():
            raise ValueError("Somente pacientes com mais de 18 anos completos podem realizar atendimentos de forma independente.")

        if not clinica.horario_funcionamento(horario_inicio, horario_fim):
            raise ValueError("Atendimento fora do horário da clínica.")

        # ID amigável de 4 dígitos
# Forçamos o ID a ser salvo como String (texto) para não perder zeros e bater com a tela
        self.__id = str(id_atendimento) if id_atendimento else str(random.randint(1000, 9999))
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo = tipo
        self.__valor_total = valor_total

    @property
    def id(self):
        return self.__id

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, nova_clinica):
        self.__clinica = nova_clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, novo_profissional):
        self.__profissional = novo_profissional

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario):
        self.__horario_inicio = horario

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario):
        self.__horario_fim = horario

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Valor inválido.")
        self.__valor_total = novo_valor

    def __str__(self):
        return f"{self.__tipo} - {self.__data}"