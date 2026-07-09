import random
from datetime import date, time

class Atendimento:
    def __init__(self, clinica, paciente, profissional, data: date, horario_inicio: time, horario_fim: time, tipo: str, valor_total: float, id_atendimento=None):

        if not paciente.eh_maior_de_idade():
            raise ValueError("Somente pacientes com mais de 18 anos completos podem realizar atendimentos de forma independente.")

        if not clinica.horario_funcionamento(horario_inicio, horario_fim):
            raise ValueError("Atendimento fora do horário da clínica.")

        self.__id = str(id_atendimento) if id_atendimento else str(random.randint(1000, 9999))
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo = tipo
        
        # O valor base da consulta agora é sagrado e não muda mais!
        self.__valor_total = valor_total
        # Eu crio essa variável para rastrear apenas o que já foi pago
        self.__valor_pago = 0.0 
        self.__procedimentos = []

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

    @property
    def procedimentos(self):
        return self.__procedimentos

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    # ---- NOVOS MÉTODOS CONTÁBEIS ABAIXO ----

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor):
        self.__valor_pago = valor

    @property
    def custo_total(self):
        # O custo real do atendimento soma o valor base + o custo de todos os procedimentos
        custo_procedimentos = sum(proc.custo for proc in self.__procedimentos)
        return self.__valor_total + custo_procedimentos

    @property
    def valor_restante(self):
        # O saldo devedor é calculado na hora: Custo Total menos o que já foi pago
        return self.custo_total - self.__valor_pago

    def __str__(self):
        return f"{self.__tipo} - {self.__data}"