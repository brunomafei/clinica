from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from view.tela_procedimento import TelaProcedimento

class ControladorProcedimento:
    def __init__(self):
        # lista de procedimentos
        self.__procedimentos = []
        self.__tela_procedimento = TelaProcedimento()

# CADASTRO --------------------------------------------------------------------------------------

    def incluir_procedimento(self, descricao, custo, profissional_responsavel, id_procedimento):
        novo_procedimento = Procedimento(descricao, custo, profissional_responsavel, id_procedimento)
        if any(procedimento.id_procedimento == id_procedimento for procedimento in self.__procedimentos):
            raise ElementoRepetidoException("Já existe um procedimento com esse ID.")
        self.__procedimentos.append(novo_procedimento)
        return novo_procedimento

# BUSCA --------------------------------------------------------------------------------------------------------------------- 

    def buscar_procedimento_por_id(self, id_procedimento):
        for procedimento in self.__procedimentos:
            if procedimento.id_procedimento == id_procedimento: 
                return procedimento
        raise ElementoNaoExisteException("Procedimento não encontrado.")
    
# LISTAGEM ------------------------------------------------------------------------------------------------------------------

    def listar_procedimentos(self):
        return self.__procedimentos
    
# LISTAGEM ------------------------------------------------------------------------------------------------------------------

    def alterar_procedimento(self, procedimento, nova_descricao, novo_custo, novo_profissional_responsavel):
        # identifica se o procedimento existe na lista de procedimentos, caso contrário lança uma exceção
        if procedimento not in self.__procedimentos:
            raise ElementoNaoExisteException("Procedimento não encontrado no sistema.")

        procedimento.descricao = nova_descricao
        procedimento.custo = novo_custo
        procedimento.profissional_responsavel = novo_profissional_responsavel
        return True
    
# REMOÇÃO ------------------------------------------------------------------------------------------------------------------

    def excluir_procedimento(self, id_procedimento):
        try:
            procedimento = self.buscar_procedimento_por_id(id_procedimento)
            self.__procedimentos.remove(procedimento)
            return True
        except ElementoNaoExisteException:
            return False
        

# TELA ------------------------------------------------------------------------------------------------------------------
    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.incluir_procedimento,
            2: self.listar_procedimentos,
            3: self.alterar_procedimento,
            4: self.excluir_procedimento,
            0: self.retornar
            
        }
        while True:
            opcao = self.__tela_procedimento.tela_opcoes()
            funcao = opcoes.get(opcao)
            
            if opcao == 0:
                funcao() 
                break
            elif funcao:
                funcao()
            else:
                self.__tela_procedimento.mostra_mensagem("Opção inválida.")