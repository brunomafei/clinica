from model.pessoa import Pessoa
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException


class ControladorPessoa:
    def __init__(self):
        self.__pessoas = []

# cadastra uma nova pessoa e adiciona na lista de pessoas
    def cadastrar_pessoa(self, nome, idade, celular, cpf):
        # Verifica se já existe alguém com esse CPF no sistema
        if self.buscar_pessoa_por_cpf(cpf) is not None:
            raise ElementoRepetidoException(f"Já existe uma pessoa cadastrada com esse CPF")
        # Se não tiver ninguém com esse CPF, cria a pessoa normalmente e adiciona na lista
        pessoa = Pessoa(nome, idade, celular, cpf)
        self.__pessoas.append(pessoa)
        return pessoa
    
# lista todas as pessoas cadastradas
    def listar_pessoas(self):
        return self.__pessoas
    
# busca pessoa pelo cpf, se não encontrar retorna None
    def buscar_pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    
    def alterar_pessoa(self, pessoa, novo_nome, nova_idade, novo_celular, novo_cpf):
        # Verifica se o objeto pessoa existe na lista de pessoas.
        if pessoa not in self.__pessoas:
            # Lança o erro e interrompe a função
            raise ElementoNaoExisteException("Pessoa não encontrada no sistema.")

        # Atualiza os dados da pessoa já cadastrada
        pessoa.__nome = novo_nome
        pessoa.__idade = nova_idade
        pessoa.__celular = novo_celular
        pessoa.__cpf = novo_cpf
        return pessoa

#remove uma pessoa da lista de pessoas

    def remover_pessoa(self, pessoa):
        if pessoa in self.__pessoas:
            self.__pessoas.remove(pessoa)
            return True
        return False