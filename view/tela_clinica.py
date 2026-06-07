class Tela_Clinica:
    def tela_opcoes(self):
        print("\n" + "="*30)
        print("--- MENU CLÍNICA ---")
        print("1 - Incluir Clínica")
        print("2 - Alterar Clínica")
        print("3 - Listar Clínicas")
        print("4 - Excluir Clínica")
        print("0 - Retornar")
        print("="*30)

        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_clinica(self):
        print("\n--- DADOS DA CLÍNICA ---")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        horario_abertura = input("Horário de Abertura (ex: 08:00): ")
        horario_fechamento = input("Horário de Fechamento (ex: 18:00): ")

        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento
        }

    def mostra_clinica(self, clinicas):
        print("\n--- LISTA DE CLÍNICAS ---")
        for clinica in clinicas:
            print(f"Nome: {clinica.nome} | Cidade: {clinica.cidade}")
            print(
                f"Horário: {clinica.horario_abertura} às {clinica.horario_fechamento}")
            print(f"Descrição: {clinica.descricao}")
            print("-" * 30)

    def seleciona_clinica(self):
        nome = input("Digite o NOME da clínica que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(f"\n>>> {msg}")
