from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from view.tela_procedimento import TelaProcedimento


class ControladorProcedimento:
    def __init__(self):
        self.__procedimentos = []
        self.__tela_procedimento = TelaProcedimento()

    def incluir_procedimento(self):
        dados = self.__tela_procedimento.pega_dados_procedimento()
        try:
            novo_procedimento = Procedimento(
                dados['descricao'], dados['custo'], dados['profissional_responsavel'], dados['id_procedimento'])
            if any(procedimento.id_procedimento == dados['id_procedimento'] for procedimento in self.__procedimentos):
                raise ElementoRepetidoException(
                    "Já existe um procedimento com esse ID.")
            self.__procedimentos.append(novo_procedimento)
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento incluído com sucesso.")
        except ElementoRepetidoException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Este elemento já existe. Tente novamente.")

    def buscar_procedimento_por_id(self, id_procedimento):
        for procedimento in self.__procedimentos:
            if procedimento.id_procedimento == id_procedimento:
                return procedimento
        raise ElementoNaoExisteException("Procedimento não encontrado.")

    def listar_procedimentos(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem(
                "Nenhum procedimento cadastrado.")
            return []
        self.__tela_procedimento.mostra_procedimentos(self.__procedimentos)
        return self.__procedimentos

    def alterar_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        try:
            procedimento = self.buscar_procedimento_por_id(id_sel)
            dados = self.__tela_procedimento.pega_dados_procedimento()
            procedimento.descricao = dados['descricao']
            procedimento.custo = dados['custo']
            procedimento.profissional_responsavel = dados['profissional_responsavel']
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento alterado com sucesso.")
        except ElementoNaoExisteException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Elemento não encontrado.")

    def excluir_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        try:
            procedimento = self.buscar_procedimento_por_id(id_sel)
            self.__procedimentos.remove(procedimento)
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
