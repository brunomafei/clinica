
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
            # Chamamos a tela em vez de usar input()
            novos_dados = self.__tela_pessoa.pega_dados_alteracao_pessoa(pessoa)

            if novos_dados is not None:
                try:
                    novo_cpf = novos_dados["cpf"]
                    # Verifica se mudou de CPF e se o novo já existe
                    if pessoa.cpf != novo_cpf and self.buscar_pessoa_por_cpf(novo_cpf) is not None:
                        raise ElementoRepetidoException(
                            "O novo CPF informado já pertence a outra pessoa.")

                    # Se o CPF mudar, precisamos remover o registro antigo do DAO antes de salvar o novo
                    cpf_antigo = pessoa.cpf
                    if cpf_antigo != novo_cpf:
                        self.__pessoas_dao.remove(cpf_antigo)

                    pessoa.nome = novos_dados["nome"]
                    pessoa.celular = novos_dados["celular"]
                    pessoa.cpf = novo_cpf

                    if isinstance(pessoa, Paciente):
                        pessoa.idade = novos_dados["idade"]

                    elif isinstance(pessoa, Profissional):
                        pessoa.especialidade = novos_dados["especialidade"]
                        pessoa.registro = novos_dados["registro"]

                    # Atualiza o objeto no DAO com a nova chave (CPF)
                    self.__pessoas_dao.add(pessoa)

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
