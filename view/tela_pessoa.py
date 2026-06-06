from model.pessoa import Paciente, Profissional

class TelaPessoa:

# Tela opções para o usuário escolher a ação desejada----------------------------
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

# Método para pegar dados do paciente------------------------------------------
    def pega_dados_paciente(self):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        celular = input("Celular: ")
        cpf = input("CPF: ")
        return nome, idade, celular, cpf

# Método para pegar dados do profissional----------------------------------------
    def pega_dados_profissional(self):
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro profissional: ")
        return nome, celular, cpf, especialidade, registro

# Método para selecionar pessoa por CPF------------------------------------------------------
    def seleciona_cpf(self):
        return input("CPF da pessoa: ")

# Método para mostrar pessoas cadastradas------------------------------------------------------
    def mostra_pessoas(self, pessoas):
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print("\nPessoas cadastradas:")
        for pessoa in pessoas:
            self.mostra_pessoa(pessoa)
            print("-" * 30)

# Método para mostrar detalhes de uma pessoa específica------------------------------------------------------
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

# Método para mostrar mensagens para o usuário------------------------------------------------------
    def mostra_mensagem(self, msg):
        print(msg)