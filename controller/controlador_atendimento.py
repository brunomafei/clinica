from model.atendimento import Atendimento
from view.tela_atendimento import Tela_Atendimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from daos.atendimento_dao import AtendimentoDAO


class ControladorAtendimento:
    def __init__(self, controlador_pessoa, controlador_clinica):
        self.__atendimentos_dao = AtendimentoDAO()
        self.__tela_atendimento = Tela_Atendimento()
        self.__controlador_pessoa = controlador_pessoa
        self.__controlador_clinica = controlador_clinica

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_atendimento,
            2: self.alterar_atendimento,
            3: self.listar_atendimentos,
            4: self.excluir_atendimento
        }

        while True:
            opcao = self.__tela_atendimento.tela_opcoes()
            if opcao == 0:
                break

            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_atendimento.mostra_mensagem("Opção inválida!")

    def incluir_atendimento(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()

        if dados is not None:
            try:
                paciente = self.__controlador_pessoa.buscar_paciente_por_cpf(
                    dados["cpf_paciente"])
                profissional = self.__controlador_pessoa.buscar_profissional_por_registro(
                    dados["registro_profissional"])
                clinica = self.__controlador_clinica.buscar_clinica_por_nome(
                    dados["nome_clinica"])

                if paciente is None or profissional is None or clinica is None:
                    raise ElementoNaoExisteException(
                        "Paciente, Profissional ou Clínica não encontrados no sistema.")

                # REQUISITO 1: Validação de maioridade do paciente
                if paciente.idade < 18:
                    raise ValueError("Somente pacientes com mais de 18 anos completos podem realizar atendimentos de forma independente.")

                # REQUISITO 2: Validação de horário de funcionamento da clínica
                if dados["hora_inicio"] < clinica.horario_abertura or dados["hora_fim"] > clinica.horario_fechamento:
                    raise ValueError(f"O atendimento deve ocorrer dentro do período de funcionamento da clínica ({clinica.horario_abertura} às {clinica.horario_fechamento}).")

                if dados["hora_inicio"] >= dados["hora_fim"]:
                    raise ValueError("A hora de início deve ser menor que a hora de término.")

                novo_atendimento = Atendimento(
                    clinica, paciente, profissional,
                    dados["data"], dados["hora_inicio"], dados["hora_fim"],
                    dados["tipo"], dados["valor_total"]
                )
                self.__atendimentos_dao.add(novo_atendimento)
                self.__tela_atendimento.mostra_mensagem(
                    "Atendimento agendado com sucesso!")
            except Exception as e:
                self.__tela_atendimento.mostra_mensagem(
                    f"Erro ao agendar: {e}")

    def alterar_atendimento(self):
        self.listar_atendimentos()
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()

        if id_atendimento is not None:
            try:
                atendimento = self.buscar_atendimento_por_id(id_atendimento)
                if atendimento is None:
                    raise ElementoNaoExisteException(
                        "Atendimento não encontrado para alteração.")

                novos_dados = self.__tela_atendimento.pega_dados_atendimento()

                if novos_dados is not None:
                    # Validação de horário também na alteração baseada na clínica já associada
                    if novos_dados["hora_inicio"] < atendimento.clinica.horario_abertura or novos_dados["hora_fim"] > atendimento.clinica.horario_fechamento:
                        raise ValueError(f"O horário deve estar dentro do período de funcionamento da clínica ({atendimento.clinica.horario_abertura} às {atendimento.clinica.horario_fechamento}).")

                    atendimento.data = novos_dados["data"]
                    atendimento.horario_inicio = novos_dados["hora_inicio"]
                    atendimento.horario_fim = novos_dados["hora_fim"]
                    atendimento.tipo = novos_dados["tipo"]
                    atendimento.valor_total = novos_dados["valor_total"]
                    
                    self.__atendimentos_dao.add(atendimento)
                    self.__tela_atendimento.mostra_mensagem(
                        "Atendimento alterado com sucesso!")
            except Exception as e:
                self.__tela_atendimento.mostra_mensagem(str(e))

    def excluir_atendimento(self):
        self.listar_atendimentos()
        id_atendimento = self.__tela_atendimento.seleciona_atendimento()

        if id_atendimento is not None:
            try:
                atendimento = self.buscar_atendimento_por_id(id_atendimento)
                if atendimento is None:
                    raise ElementoNaoExisteException(
                        "Atendimento não encontrado.")

                self.__atendimentos_dao.remove(atendimento.id)
                self.__tela_atendimento.mostra_mensagem(
                    "Atendimento excluído com sucesso!")
            except Exception as e:
                self.__tela_atendimento.mostra_mensagem(str(e))

    def listar_atendimentos(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if len(atendimentos) == 0:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum atendimento agendado.")
        else:
            self.__tela_atendimento.mostra_atendimento(atendimentos)
        return atendimentos

    def buscar_atendimento_por_id(self, id_buscado):
        return self.__atendimentos_dao.get(id_buscado)