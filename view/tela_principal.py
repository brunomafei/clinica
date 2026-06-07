
class TelaPrincipal:

# Tela opções para o usuário escolher a ação desejada----------------------------
    def tela_opcoes(self):
        print("\n--- Menu Principal ---")
        print("1. Atendimentos")
        print("2. Clínicas")
        print("3. Pagamentos")
        print("4. Pessoas")
        print("5. Procedimentos")
        print("6. Relatórios")
        print("0. Sair")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

# Método para mostrar mensagens para o usuário------------------------------------------------------
    def mostra_mensagem(self, mensagem):
        print(mensagem)
