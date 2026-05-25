from controlador_atendimento import Atendimento


class ControladorAtendimento:
    # Ele recebe o Controlador de Pagamento no construtor para poder conversar com ele
    def __init__(self, controlador_pagamento):
        self.__atendimentos = []
        self.__controlador_pagamento = controlador_pagamento

    def incluir_atendimento(self, clinica, paciente, profissional, data, hora_inicio, hora_fim, tipo, valor_total):
        try:
            # Regra de negócio 1: Validar se o paciente é maior de 18 anos
            # (Presumindo que você criou o método eh_maior_de_idade() na classe Paciente do UML)
            if not paciente.eh_maior_de_idade():
                raise ValueError("O paciente precisa ser maior de 18 anos.")

            # Regra de negócio 2: O Model já valida se o horário bate com o da clínica.
            # Se não bater, o Atendimento(...) vai jogar o ValueError aqui pro except.
            novo_atendimento = Atendimento(
                clinica, paciente, profissional,
                data, hora_inicio, hora_fim, tipo, valor_total
            )

            self.__atendimentos.append(novo_atendimento)
            return novo_atendimento

        except ValueError as e:
            # Segura as broncas tanto da idade quanto do horário da clínica
            print(f"Erro ao agendar atendimento: {e}")
            return None

    def listar_atendimentos(self):
        return self.__atendimentos

    def alterar_atendimento(self, atendimento, nova_data, nova_hora_inicio, nova_hora_fim, novo_valor):
        try:
            # Atualiza os dados passando pelas proteções dos setters
            atendimento.data = nova_data
            atendimento.horario_inicio = nova_hora_inicio
            atendimento.horario_fim = nova_hora_fim
            atendimento.valor_total = novo_valor
            return True
        except ValueError as e:
            print(f"Erro ao alterar o agendamento: {e}")
            return False

    def excluir_atendimento(self, atendimento):
        if atendimento in self.__atendimentos:
            self.__atendimentos.remove(atendimento)
            return True
        return False
