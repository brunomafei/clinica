
class TelaProcedimento:

    def tela_opcoes(self):
        print("\n--- Procedimentos ---")
        print("1. Incluir Procedimento")
        print("2. Listar Procedimentos")
        print("3. Alterar Procedimento")
        print("4. Excluir Procedimento")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def pega_dados_procedimento(self):
        print("\n--- Cadastro de Procedimento ---")

        descricao = input("Descrição do procedimento: ")
        custo = float(input("Custo do procedimento: "))
        profissional_responsavel = input("Profissional responsável: ")
        try:
            id_procedimento = int(input("ID do procedimento: "))
        except ValueError:
            id_procedimento = input("ID do procedimento: ")

        return {"descricao": descricao, "custo": custo, "profissional_responsavel": profissional_responsavel, "id_procedimento": id_procedimento}

    def mostra_procedimentos(self, procedimentos):
        print("\n--- Lista de Procedimentos ---")
        for procedimento in procedimentos:
            prof = procedimento.profissional_responsavel
            nome_prof = getattr(prof, 'nome', prof)
            print(f"ID: {procedimento.id_procedimento} | Descrição: {procedimento.descricao} | Custo: {procedimento.custo} | Profissional Responsável: {nome_prof}")

    def seleciona_procedimento(self):
        try:
            id_procedimento = int(input("Digite o ID do procedimento: "))
        except ValueError:
            id_procedimento = input("Digite o ID do procedimento: ")
        return id_procedimento

    def mostra_mensagem(self, mensagem):
        print(mensagem)
