
from model.pessoa import Paciente    
from model.pessoa import Profissional
from view.tela_pessoa import TelaPessoa
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException

class ControladorPessoa:
    def __init__(self):
        # lista de pacientes e profissionais
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()

# CADASTRO --------------------------------------------------------------------------------------
    # Cadastra Paciente
    def cadastrar_paciente(self, nome, idade, celular, cpf):
        if self.buscar_pessoa_por_cpf(cpf) is not None:
            raise ElementoRepetidoException("Já existe uma pessoa cadastrada com esse CPF.")
        
        # Cria um PACIENTE e adiciona na lista
        paciente = Paciente(nome, celular, cpf, idade)
        self.__pessoas.append(paciente)
        return paciente

    # Cadastra Profissional
    def cadastrar_profissional(self, nome, celular, cpf, especialidade, registro):
        if self.buscar_pessoa_por_cpf(cpf) is not None:
            raise ElementoRepetidoException("Já existe uma pessoa cadastrada com esse CPF.")
        
        # Cria um PROFISSIONAL e adiciona na lista
        profissional = Profissional(nome, celular, cpf, especialidade, registro)
        self.__pessoas.append(profissional)
        return profissional

# LISTAGEM ------------------------------------------------------------------------------------------------------------------

    def listar_pessoas(self):
        return self.__pessoas

# BUSCA --------------------------------------------------------------------------------------------------------------------- 

    def buscar_pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoas:
            
            if pessoa.cpf == cpf: 
                return pessoa
        return None
    
# ATUALIZAÇÃO ------------------------------------------------------------------------------------------------------------------   
#  
    def alterar_pessoa(self, pessoa, novo_nome, novo_celular, novo_cpf, nova_idade=None, nova_especialidade=None, novo_registro=None):
        #identifica se a pessoa existe na lista de pessoas, caso contrário lança uma exceção
        if pessoa not in self.__pessoas:
            raise ElementoNaoExisteException("Pessoa não encontrada no sistema.")

        # identifica se o cpf e diferente do atual e se já existe outra pessoa com o novo cpf
        if pessoa.cpf != novo_cpf and self.buscar_pessoa_por_cpf(novo_cpf) is not None:
            raise ElementoRepetidoException("O novo CPF informado já pertence a outra pessoa.")
        
        # Atualiza os dados comuns
        pessoa.nome = novo_nome
        pessoa.celular = novo_celular
        pessoa.cpf = novo_cpf

        # Atualiza os dados específicos com base no tipo da pessoa
        if isinstance(pessoa, Paciente):
            if nova_idade is not None:
                pessoa.idade = nova_idade
                
        elif isinstance(pessoa, Profissional):
            if nova_especialidade is not None:
                pessoa.especialidade = nova_especialidade
            if novo_registro is not None:
                pessoa.registro = novo_registro
                
        return pessoa

# REMOÇÃO ------------------------------------------------------------------------------------------------------------------
    def remover_pessoa(self, pessoa):
        if pessoa in self.__pessoas:
            self.__pessoas.remove(pessoa)
            return True
        return False

# TELA ------------------------------------------------------------------------------------------------------------------
    def retornar(self):
        return

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_paciente, 
            2: self.cadastrar_profissional, 
            3: self.alterar_pessoa, 
            4: self.listar_pessoas, 
            5: self.remover_pessoa, 
            0: self.retornar
        }
        while True:
            opcao = self.__tela_pessoa.tela_opcoes()
            funcao = opcoes.get(opcao)
            
            if opcao == 0:
                funcao() # type: ignore
                break
            elif funcao:
                funcao()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida.")