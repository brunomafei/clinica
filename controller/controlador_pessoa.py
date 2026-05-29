from model.pessoa import Pessoa
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from exceptions.elemento_repetido_exception import ElementoRepetidoException


class ControladorPessoa:
    def __init__(self):
        self.pessoas = []

# cadastra uma nova pessoa e adiciona na lista de pessoas
    def cadastrar_pessoa(self, nome, idade, celular, cpf):
        pessoa = Pessoa(nome, idade, celular, cpf)
        self.pessoas.append(pessoa)
        return pessoa
    
# lista todas as pessoas cadastradas
    def listar_pessoas(self):
        return self.pessoas
    
# busca pessoa pelo cpf, se não encontrar retorna None
    def buscar_pessoa_por_cpf(self, cpf):
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    
    def alterar_pessoa(self, pessoa, novo_nome, nova_idade, novo_celular, novo_cpf):
        # Verifica se o objeto pessoa existe na lista de pessoas.
        if pessoa not in self.pessoas:
            # Lança o erro e interrompe a função
            raise ElementoNaoExisteException("Pessoa não encontrada no sistema.")

        # Atualiza os dados da pessoa já cadastrada
        pessoa.nome = novo_nome
        pessoa.idade = nova_idade
        pessoa.celular = novo_celular
        pessoa.cpf = novo_cpf
        return pessoa

#remove uma pessoa da lista de pessoas

    def remover_pessoa(self, pessoa):
        if pessoa in self.pessoas:
            self.pessoas.remove(pessoa)
            return True
        return False