from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from view.tela_procedimento import TelaProcedimento
from daos.procedimento_dao import ProcedimentoDAO


class ControladorProcedimento:
    def __init__(self):
        self.__procedimentos_dao = ProcedimentoDAO()
        self.__tela_procedimento = TelaProcedimento()

# Inclusão de um novo procedimento, verificando se já existe um procedimento com o mesmo ID para evitar duplicidade---------------------------------------------------------------------------------------
    def incluir_procedimento(self):
        dados = self.__tela_procedimento.pega_dados_procedimento()
        try:
            novo_procedimento = Procedimento(
                dados['descricao'], dados['custo'], dados['profissional_responsavel'], dados['id_procedimento'])
            if self.__procedimentos_dao.get(dados['id_procedimento']) is not None:
                raise ElementoRepetidoException(
                    "Já existe um procedimento com esse ID.")
            self.__procedimentos_dao.add(novo_procedimento)
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento incluído com sucesso.")
        except ElementoRepetidoException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Este elemento já existe. Tente novamente.")

# Busca um procedimento pelo ID, lançando uma exceção caso o procedimento não seja encontrado---------------------------------------------------------------------------------------
    def buscar_procedimento_por_id(self, id_procedimento):
        procedimento = self.__procedimentos_dao.get(id_procedimento)
        if procedimento is None:
            raise ElementoNaoExisteException("Procedimento não encontrado.")
        return procedimento

# Lista todos os procedimentos cadastrados, mostrando uma mensagem caso não haja procedimentos para listar---------------------------------------------------------------------------------------
    def listar_procedimentos(self):
        procedimentos = list(self.__procedimentos_dao.get_all())
        if not procedimentos:
            self.__tela_procedimento.mostra_mensagem(
                "Nenhum procedimento cadastrado.")
            return []
        self.__tela_procedimento.mostra_procedimentos(procedimentos)
        return procedimentos

# Altera os dados de um procedimento existente, verificando se o procedimento existe antes de tentar alterá-lo---------------------------------------------------------------------------------------
    def alterar_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        try:
            procedimento = self.buscar_procedimento_por_id(id_sel)
            dados = self.__tela_procedimento.pega_dados_procedimento()
            procedimento.descricao = dados['descricao']
            procedimento.custo = dados['custo']
            procedimento.profissional_responsavel = dados['profissional_responsavel']
            self.__procedimentos_dao.add(procedimento)
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento alterado com sucesso.")
        except ElementoNaoExisteException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Elemento não encontrado.")

# Exclui um procedimento existente, verificando se o procedimento existe antes de tentar excluí-lo---------------------------------------------------------------------------------------
    def excluir_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        try:
            procedimento = self.buscar_procedimento_por_id(id_sel)
            self.__procedimentos_dao.remove(id_sel)
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento excluído com sucesso.")
        except ElementoNaoExisteException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Elemento não encontrado.")

    def retornar(self):
        return

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_procedimento,
            2: self.listar_procedimentos,
            3: self.alterar_procedimento,
            4: self.excluir_procedimento,
            0: self.retornar
        }

        continua = True

        while continua:
            opcao = self.__tela_procedimento.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_procedimento.mostra_mensagem(" Opção inválida!")

            if opcao == 0:
                continua = False
