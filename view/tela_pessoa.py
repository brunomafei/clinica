from model.pessoa import Paciente, Profissional


class TelaPessoa:

    def tela_opcoes(self):
        print("\n--- Pessoas ---")
        print("1 - Cadastrar paciente")
        print("2 - Cadastrar profissional")
        print("3 - Alterar pessoa")
        print("4 - Listar pessoas")
        print("5 - Remover pessoa")
        print("0 - Voltar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_paciente(self):
        nome = input("Nome: ")
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except ValueError:
                print(" Digite um número válido!")
                # loop para um int
        celular = input("Celular: ")
        cpf = input("CPF: ")
        return nome, idade, celular, cpf

    def pega_dados_profissional(self):
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro profissional: ")
        return nome, celular, cpf, especialidade, registro

    def seleciona_cpf(self):
        return input("CPF da pessoa: ")

    def mostra_pessoas(self, pessoas):
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print("\nPessoas cadastradas:")
        for pessoa in pessoas:
            self.mostra_pessoa(pessoa)
            print("-" * 30)

    def mostra_pessoa(self, pessoa):
        tipo = "Paciente" if isinstance(pessoa, Paciente) else "Profissional"
        print(f"Tipo: {tipo}")
        print(f"Nome: {pessoa.nome}")
        print(f"Celular: {pessoa.celular}")
        print(f"CPF: {pessoa.cpf}")

        if isinstance(pessoa, Paciente):
            print(f"Idade: {pessoa.idade}")
        elif isinstance(pessoa, Profissional):
            print(f"Especialidade: {pessoa.especialidade}")
            print(f"Registro: {pessoa.registro}")

    def mostra_mensagem(self, msg):
        print(msg)
