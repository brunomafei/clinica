from model.pessoa import Paciente, Profissional
from view.tela_pessoa import TelaPessoa
from exceptions.elemento_repetido_exception import ElementoRepetidoException
from daos.pessoa_dao import PessoaDAO


class ControladorPessoa:
    """Responsável por coordenar as operações de cadastro,
    alteração, listagem e remoção de pessoas."""

    def __init__(self):
        # Instancia o repositório de pessoas e a interface com o usuário.
        self.__pessoas_dao = PessoaDAO()
        self.__tela_pessoa = TelaPessoa()

    def cadastrar_paciente(self):
        """Coleta os dados do paciente e salva no DAO após validar o CPF
        e a idade."""
        dados = self.__tela_pessoa.pega_dados_paciente()

        if dados is not None:
            try:
                # A idade vem como texto na tela e precisa ser convertida.
                idade = int(dados["idade"])
                cpf = dados["cpf"]

                # Garante que não exista outra pessoa com o mesmo CPF.
                if self.buscar_pessoa_por_cpf(cpf) is not None:
                    raise ElementoRepetidoException(
                        "Já existe uma pessoa cadastrada com esse CPF."
                    )

                paciente = Paciente(dados["nome"], dados["celular"], cpf, idade)
                self.__pessoas_dao.add(paciente)
                self.__tela_pessoa.mostra_mensagem("Paciente cadastrado com sucesso.")

            except ValueError:
                self.__tela_pessoa.mostra_mensagem(
                    "Erro: A idade deve ser um número inteiro!"
                )
            except ElementoRepetidoException as e:
                self.__tela_pessoa.mostra_mensagem(str(e))

    def cadastrar_profissional(self):
        """Coleta os dados do profissional e salva no DAO,
        evitando CPF duplicado."""
        dados = self.__tela_pessoa.pega_dados_profissional()

        if dados is not None:
            try:
                cpf = dados["cpf"]

                # CPF é a chave principal usada para identificar cada pessoa.
                if self.buscar_pessoa_por_cpf(cpf) is not None:
                    raise ElementoRepetidoException(
                        "Já existe uma pessoa cadastrada com esse CPF."
                    )

                profissional = Profissional(
                    dados["nome"],
                    dados["celular"],
                    cpf,
                    dados["especialidade"],
                    dados["registro"],
                )
                self.__pessoas_dao.add(profissional)
                self.__tela_pessoa.mostra_mensagem("Profissional cadastrado com sucesso.")

            except ElementoRepetidoException as e:
                self.__tela_pessoa.mostra_mensagem(str(e))

    def listar_pessoas(self):
        """Exibe todas as pessoas cadastradas ou uma mensagem quando
        não houver nenhuma."""
        pessoas = list(self.__pessoas_dao.get_all())
        if not pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return
        self.__tela_pessoa.mostra_pessoas(pessoas)

    def buscar_pessoa_por_cpf(self, cpf):
        """Retorna uma pessoa pelo CPF, caso exista no DAO."""
        return self.__pessoas_dao.get(cpf)

    def buscar_paciente_por_cpf(self, cpf):
        """Retorna o paciente correspondente ao CPF, se ele for realmente um paciente."""
        pessoa = self.buscar_pessoa_por_cpf(cpf)
        if isinstance(pessoa, Paciente):
            return pessoa
        return None

    def buscar_profissional_por_registro(self, registro):
        """Busca um profissional pelo número de registro."""
        for pessoa in self.__pessoas_dao.get_all():
            if isinstance(pessoa, Profissional) and pessoa.registro == registro:
                return pessoa
        return None

    def alterar_pessoa(self):
        """Permite alterar os dados de uma pessoa já cadastrada,
        preservando o tipo correto."""
        cpf_antigo = self.__tela_pessoa.seleciona_cpf()
        if cpf_antigo is None:
            return  # Usuário cancelou a seleção.

        pessoa = self.buscar_pessoa_por_cpf(cpf_antigo)

        if pessoa is None:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")
            return

        # O fluxo de alteração depende do tipo da pessoa: paciente ou profissional.
        if isinstance(pessoa, Paciente):
            dados = self.__tela_pessoa.pega_dados_paciente()

            if dados is not None:
                try:
                    nova_idade = int(dados["idade"])
                    novo_cpf = dados["cpf"]

                    # Se o CPF mudou, é preciso garantir que ele não pertença
                    # a outra pessoa.
                    if (
                        pessoa.cpf != novo_cpf
                        and self.buscar_pessoa_por_cpf(novo_cpf) is not None
                    ):
                        raise ElementoRepetidoException(
                            "O novo CPF informado já pertence a outra pessoa."
                        )

                    # Como o DAO usa o CPF como chave, é necessário remover a
                    # entrada antiga antes de salvar a nova.
                    self.__pessoas_dao.remove(cpf_antigo)

                    # Atualiza os atributos do objeto em memória.
                    pessoa.nome = dados["nome"]
                    pessoa.celular = dados["celular"]
                    pessoa.cpf = novo_cpf
                    pessoa.idade = nova_idade

                    # Reinsere o objeto no DAO com a chave atualizada, se o CPF
                    # tiver sido alterado.
                    self.__pessoas_dao.add(pessoa)
                    self.__tela_pessoa.mostra_mensagem("Paciente alterado com sucesso.")

                except ValueError:
                    self.__tela_pessoa.mostra_mensagem(
                        "Erro: A idade deve ser um número inteiro!"
                    )
                except ElementoRepetidoException as e:
                    self.__tela_pessoa.mostra_mensagem(str(e))

        elif isinstance(pessoa, Profissional):
            dados = self.__tela_pessoa.pega_dados_profissional()

            if dados is not None:
                try:
                    novo_cpf = dados["cpf"]

                    if pessoa.cpf != novo_cpf and self.buscar_pessoa_por_cpf(novo_cpf) is not None:
                        raise ElementoRepetidoException("O novo CPF informado já pertence a outra pessoa.")

                    self.__pessoas_dao.remove(cpf_antigo)

                    pessoa.nome = dados["nome"]
                    pessoa.celular = dados["celular"]
                    pessoa.cpf = novo_cpf
                    pessoa.especialidade = dados["especialidade"]
                    pessoa.registro = dados["registro"]

                    self.__pessoas_dao.add(pessoa)
                    self.__tela_pessoa.mostra_mensagem("Profissional alterado com sucesso.")

                except ElementoRepetidoException as e:
                    self.__tela_pessoa.mostra_mensagem(str(e))

    def remover_pessoa(self):
        """Remove uma pessoa do cadastro a partir do CPF informado."""
        cpf = self.__tela_pessoa.seleciona_cpf()
        if cpf is None:
            return

        pessoa = self.buscar_pessoa_por_cpf(cpf)

        if pessoa is not None:
            self.__pessoas_dao.remove(cpf)
            self.__tela_pessoa.mostra_mensagem("Pessoa removida com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

    def retornar(self):
        """Método de saída da tela de pessoas."""
        return

    def abre_tela(self):
        """Exibe o menu principal da área de pessoas e direciona para as
        opções escolhidas."""
        lista_opcoes = {
            1: self.cadastrar_paciente,
            2: self.cadastrar_profissional,
            3: self.alterar_pessoa,
            4: self.listar_pessoas,
            5: self.remover_pessoa,
            0: self.retornar,
        }

        continua = True
        while continua:
            opcao = self.__tela_pessoa.tela_opcoes()

            if opcao == -1 or opcao == 0:
                continua = False
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida!")