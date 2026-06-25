from model.pessoa import Paciente, Profissional


class TelaPessoa:

# método para mostrar as opções do menu de pessoas, tratando a exceção caso o usuário digite um valor inválido---------------------------------------
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

# métodos para pegar os dados dos pacientes e profissionais, tratando a exceção caso o usuário digite um valor inválido para a idade do paciente---------------------------------------
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

# método para pegar os dados dos profissionais, tratando a exceção caso o usuário digite um valor inválido para o registro do profissional---------------------------------------
    def pega_dados_profissional(self):
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro profissional: ")
        return nome, celular, cpf, especialidade, registro

# método para selecionar o CPF de uma pessoa, para ser usado na alteração e remoção de pessoas---------------------------------------------------------------------------------------
    def seleciona_cpf(self):
        return input("CPF da pessoa: ")

# método para mostrar a lista de pessoas, mostrando uma mensagem caso não haja pessoas cadastradas---------------------------------------------------------------------------------------
    def mostra_pessoas(self, pessoas):
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print("\nPessoas cadastradas:")
        for pessoa in pessoas:
            self.mostra_pessoa(pessoa)
            print("-" * 30)

# método para mostrar os dados de uma pessoa, identificando se é um paciente ou profissional e mostrando as informações correspondentes---------------------------------------------------------------------------------------
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
