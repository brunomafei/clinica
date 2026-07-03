
from model.pessoa import Paciente
from model.pessoa import Profissional
from view.tela_pessoa import TelaPessoa
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from daos.pessoa_dao import PessoaDAO


class ControladorPessoa:
    def __init__(self):
        self.__pessoas_dao = PessoaDAO()
        self.__tela_pessoa = TelaPessoa()

# metodo para cadastrar um paciente, verificando se já existe um paciente com o mesmo CPF para evitar duplicidade---------------------------------------------------------------------------------------
    def cadastrar_paciente(self):
        nome, idade, celular, cpf = self.__tela_pessoa.pega_dados_paciente()
        try:
            if self.buscar_pessoa_por_cpf(cpf) is not None:
                raise ElementoRepetidoException(
                    "Já existe uma pessoa cadastrada com esse CPF.")
            paciente = Paciente(nome, celular, cpf, idade)
            self.__pessoas_dao.add(paciente)
            self.__tela_pessoa.mostra_mensagem(
                "Paciente cadastrado com sucesso.")
        except ElementoRepetidoException:
            self.__tela_pessoa.mostra_mensagem(
                "Erro: Este elemento já existe. Tente novamente.")

# metodo para cadastrar um profissional, verificando se já existe um profissional com o mesmo CPF para evitar duplicidade---------------------------------------------------------------------------------------
    def cadastrar_profissional(self):
        nome, celular, cpf, especialidade, registro = self.__tela_pessoa.pega_dados_profissional()
        try:
            if self.buscar_pessoa_por_cpf(cpf) is not None:
                raise ElementoRepetidoException(
                    "Já existe uma pessoa cadastrada com esse CPF.")
            profissional = Profissional(
                nome, celular, cpf, especialidade, registro)
            self.__pessoas_dao.add(profissional)
            self.__tela_pessoa.mostra_mensagem(
                "Profissional cadastrado com sucesso.")
        except ElementoRepetidoException:
            self.__tela_pessoa.mostra_mensagem(
                "Erro: Este elemento já existe. Tente novamente.")

# metodo para listar todas as pessoas cadastradas, mostrando uma mensagem caso não haja pessoas para listar---------------------------------------------------------------------------------------
    def listar_pessoas(self):
        pessoas = list(self.__pessoas_dao.get_all())
        if not pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return
        self.__tela_pessoa.mostra_pessoas(pessoas)

# método para buscar uma pessoa pelo CPF, retornando None caso a pessoa não seja encontrada---------------------------------------------------------------------------------------
    def buscar_pessoa_por_cpf(self, cpf):
        pessoa = self.__pessoas_dao.get(cpf)
        return pessoa

# método para buscar um paciente pelo CPF, retornando None caso o paciente não seja encontrado ou caso a pessoa encontrada não seja um paciente---------------------------------------------------------------------------------------
    def buscar_paciente_por_cpf(self, cpf):
        pessoa = self.buscar_pessoa_por_cpf(cpf)
        if isinstance(pessoa, Paciente):
            return pessoa
        return None

# método para buscar um profissional pelo registro, retornando None caso o profissional não seja encontrado ou caso a pessoa encontrada não seja um profissional---------------------------------------------------------------------------------------
    def buscar_profissional_por_registro(self, registro):
        for pessoa in self.__pessoas_dao.get_all():
            if isinstance(pessoa, Profissional) and pessoa.registro == registro:
                return pessoa
        return None

# método para alterar os dados de uma pessoa existente, verificando se a pessoa existe antes de tentar alterá-la e verificando se o novo CPF já pertence a outra pessoa para evitar duplicidade---------------------------------------------------------------------------------------
    def alterar_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_cpf()
        pessoa = self.buscar_pessoa_por_cpf(cpf)

        if pessoa is not None:
            novo_nome = input("Novo nome: ")
            novo_celular = input("Novo celular: ")
            novo_cpf = input("Novo CPF: ")

            try:
                if pessoa.cpf != novo_cpf and self.buscar_pessoa_por_cpf(novo_cpf) is not None:
                    raise ElementoRepetidoException(
                        "O novo CPF informado já pertence a outra pessoa.")

                pessoa.nome = novo_nome
                pessoa.celular = novo_celular
                pessoa.cpf = novo_cpf

                if isinstance(pessoa, Paciente):
                    while True:
                        try:
                            nova_idade = int(input("Nova idade: "))
                            break
                        except ValueError:
                            print(" Digite um número válido!")
                            # loop para um int
                    nova_idade = int(input("Nova idade: "))
                    pessoa.idade = nova_idade

                elif isinstance(pessoa, Profissional):
                    nova_especialidade = input("Nova especialidade: ")
                    novo_registro = input("Novo registro: ")
                    pessoa.especialidade = nova_especialidade
                    pessoa.registro = novo_registro

                self.__tela_pessoa.mostra_mensagem(
                    "Pessoa alterada com sucesso.")
            except ElementoRepetidoException:
                self.__tela_pessoa.mostra_mensagem(
                    "Erro: Este elemento já existe. Tente novamente.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def remover_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_cpf()
        pessoa = self.buscar_pessoa_por_cpf(cpf)

        if pessoa is not None:
            self.__pessoas_dao.remove(cpf)
            self.__tela_pessoa.mostra_mensagem("Pessoa removida com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def retornar(self):
        return

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_paciente,
            2: self.cadastrar_profissional,
            3: self.alterar_pessoa,
            4: self.listar_pessoas,
            5: self.remover_pessoa,
            0: self.retornar
        }

        continua = True

        while continua:
            opcao = self.__tela_pessoa.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_pessoa.mostra_mensagem(" Opção inválida!")

            if opcao == 0:
                continua = False
