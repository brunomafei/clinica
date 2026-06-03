
class TelaProcedimento:

# Opçoes de tela----------------------------------------------------------------------

    def tela_opcoes(self):
        print("\n--- Procedimentos ---")
        print("1. Incluir Procedimento")
        print("2. Listar Procedimentos")
        print("3. Alterar Procedimento")
        print("4. Excluir Procedimento")
        print("0. Voltar")
        
        return input("Escolha uma opção: ")

# Métodos para interagir com o usuário ----------------------------------------------------------------------

    def pega_dados_procedimento(self):
        print("\n--- Cadastro de Procedimento ---")

        descricao = input("Descrição do procedimento: ")
        custo = float(input("Custo do procedimento: "))
        profissional_responsavel = input("Profissional responsável: ")
        id_procedimento = input("ID do procedimento: ")

        return {"descricao": descricao, "custo": custo, "profissional_responsavel": profissional_responsavel, "id_procedimento": id_procedimento}

# Métodos para exibir informações ----------------------------------------------------------------------

    def mostra_procedimentos(self, procedimentos):
        print("\n--- Lista de Procedimentos ---")
        for procedimento in procedimentos:
            print(f"ID: {procedimento.id_procedimento} | Descrição: {procedimento.descricao} | Custo: {procedimento.custo} | Profissional Responsável: {procedimento.profissional_responsavel.nome}")

# pega procedimento pelo id--------------------------------------------------------------------------------
    def seleciona_procedimento(self):
        id_procedimento = input("Digite o ID do procedimento: ")
        return id_procedimento

# mostra mensagem-----------------------------------------------------------------------------------------
   
    def mostra_mensagem(self, mensagem):
        print(mensagem)