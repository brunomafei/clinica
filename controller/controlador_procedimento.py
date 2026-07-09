from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from view.tela_procedimento import TelaProcedimento
from daos.procedimento_dao import ProcedimentoDAO

class ControladorProcedimento:
    def __init__(self):
        self.__procedimentos_dao = ProcedimentoDAO()
        self.__tela_procedimento = TelaProcedimento()

    def incluir_procedimento(self):
        dados = self.__tela_procedimento.pega_dados_procedimento()
        if dados is None: return
        
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

    def buscar_procedimento_por_id(self, id_procedimento):
        procedimento = self.__procedimentos_dao.get(id_procedimento)
        if procedimento is None:
            raise ElementoNaoExisteException("Procedimento não encontrado.")
        return procedimento

    def listar_procedimentos(self):
        procedimentos = list(self.__procedimentos_dao.get_all())
        if not procedimentos:
            self.__tela_procedimento.mostra_mensagem(
                "Nenhum procedimento cadastrado.")
            return []
        self.__tela_procedimento.mostra_procedimentos(procedimentos)
        return procedimentos

    def alterar_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        if id_sel is None: return
        
        try:
            procedimento = self.buscar_procedimento_por_id(id_sel)
            dados = self.__tela_procedimento.pega_dados_procedimento()
            if dados is None: return
            
            procedimento.descricao = dados['descricao']
            procedimento.custo = dados['custo']
            procedimento.profissional_responsavel = dados['profissional_responsavel']
            self.__procedimentos_dao.add(procedimento)
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento alterado com sucesso.")
        except ElementoNaoExisteException:
            self.__tela_procedimento.mostra_mensagem(
                "Erro: Elemento não encontrado.")

    def excluir_procedimento(self):
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        if id_sel is None: return
        
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
                if opcao != -1: # Ignora aviso se apenas fechar a janela
                    self.__tela_procedimento.mostra_mensagem(" Opção inválida!")

            if opcao in (0, -1):
                continua = False

    def selecionar_procedimento_existente(self):
        # Eu crio este método para ser chamado por outros controladores.
        # Ele lista o catálogo, pede para o usuário selecionar um ID e retorna o objeto do Procedimento.
        self.listar_procedimentos()
        id_sel = self.__tela_procedimento.seleciona_procedimento()
        
        if id_sel is not None:
            try:
                return self.buscar_procedimento_por_id(id_sel)
            except ElementoNaoExisteException:
                self.__tela_procedimento.mostra_mensagem("Erro: Procedimento não encontrado no catálogo.")
        return None