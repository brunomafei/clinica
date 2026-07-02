from model.clinica import Clinica
from view.tela_clinica import Tela_Clinica
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from daos.clinica_dao import ClinicaDAO


class ControladorClinica:
    def __init__(self):
        self.__clinicas_dao = ClinicaDAO()
        self.__tela_clinica = Tela_Clinica()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_clinica,
            2: self.alterar_clinica,
            3: self.listar_clinicas,
            4: self.excluir_clinica
        }

        while True:
            opcao = self.__tela_clinica.tela_opcoes()
            if opcao == 0:
                break

            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_clinica.mostra_mensagem("Opção inválida!")

    def incluir_clinica(self):
        dados = self.__tela_clinica.pega_dados_clinica()

        if dados is not None:
            try:
                if self.buscar_clinica_por_nome(dados["nome"]) is not None:
                    raise ElementoRepetidoException(
                        f"A clínica '{dados['nome']}' já está cadastrada!")

                nova_clinica = Clinica(
                    dados["nome"], dados["cidade"], dados["descricao"],
                    dados["horario_abertura"], dados["horario_fechamento"]
                )
                self.__clinicas_dao.add(nova_clinica)
                self.__tela_clinica.mostra_mensagem(
                    "Clínica cadastrada com sucesso!")
            except Exception as e:
                self.__tela_clinica.mostra_mensagem(f"Erro: {e}")

    def alterar_clinica(self):
        self.listar_clinicas()
        nome_clinica = self.__tela_clinica.seleciona_clinica()

        if nome_clinica is not None:
            try:
                clinica = self.buscar_clinica_por_nome(nome_clinica)
                if clinica is None:
                    raise ElementoNaoExisteException(
                        "Clínica não encontrada para alteração.")

                novos_dados = self.__tela_clinica.pega_dados_clinica()

                if novos_dados is not None:
                    clinica.nome = novos_dados["nome"]
                    clinica.cidade = novos_dados["cidade"]
                    clinica.descricao = novos_dados["descricao"]
                    clinica.horario_abertura = novos_dados["horario_abertura"]
                    clinica.horario_fechamento = novos_dados["horario_fechamento"]
                    self.__clinicas_dao.add(clinica)

                    self.__tela_clinica.mostra_mensagem(
                        "Clínica alterada com sucesso!")
            except Exception as e:
                self.__tela_clinica.mostra_mensagem(str(e))

    def excluir_clinica(self):
        self.listar_clinicas()
        nome_clinica = self.__tela_clinica.seleciona_clinica()

        if nome_clinica is not None:
            try:
                clinica = self.buscar_clinica_por_nome(nome_clinica)
                if clinica is None:
                    raise ElementoNaoExisteException(
                        f"Não encontramos nenhuma clínica com o nome '{nome_clinica}'.")

                self.__clinicas_dao.remove(nome_clinica)
                self.__tela_clinica.mostra_mensagem(
                    "Clínica excluída com sucesso!")
            except Exception as e:
                self.__tela_clinica.mostra_mensagem(str(e))

    def listar_clinicas(self):
        clinicas = list(self.__clinicas_dao.get_all())
        if len(clinicas) == 0:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
        else:
            self.__tela_clinica.mostra_clinica(clinicas)

    def buscar_clinica_por_nome(self, nome):
        clinica = self.__clinicas_dao.get(nome)
        return clinica
