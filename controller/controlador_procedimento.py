from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorProcedimento:
    def __init__(self):
        # lista de procedimentos
        self.__procedimentos = []

# CADASTRO --------------------------------------------------------------------------------------

    def incluir_procedimento(self, descricao, custo, profissional_responsavel):
        novo_procedimento = Procedimento(descricao, custo, profissional_responsavel)
        self.__procedimentos.append(novo_procedimento)
        return novo_procedimento

# BUSCA --------------------------------------------------------------------------------------------------------------------- 

    def buscar_procedimento_por_id(self, id_procedimento):
        for procedimento in self.__procedimentos:
            if procedimento.id_procedimento == id_procedimento: 
                return procedimento
        return None
    
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

    def excluir_procedimento(self, procedimento):
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)
            return True
        return False