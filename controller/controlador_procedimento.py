from model.procedimento import Procedimento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorProcedimento:
    def __init__(self):
        # lista de procedimentos
        self.__procedimentos = []

# CADASTRO --------------------------------------------------------------------------------------

    def incluir_procedimento(self, descricao, custo, profissional_responsavel, id_procedimento):
        novo_procedimento = Procedimento(descricao, custo, profissional_responsavel, id_procedimento)
        if id_procedimento in self.__procedimentos:
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