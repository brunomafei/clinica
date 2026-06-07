class Tela_Pagamento:
    def tela_opcoes(self):
        print("\n" + "="*30)
        print("--- MENU PAGAMENTO ---")
        print("1 - Registrar Pagamento")
        print("2 - Listar Pagamentos")
        print("0 - Retornar")
        print("="*30)

        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_pagamento(self):
        print("\n--- DADOS DO PAGAMENTO ---")
        id_atendimento = input("ID ou Data do Atendimento que será pago: ")
        data = input("Data do pagamento (DD/MM/AAAA): ")

        try:
            valor = float(input("Valor a ser pago: R$ "))
        except ValueError:
            print(">>> Erro: Valor deve ser numérico!")
            return None

        print("\nTipos disponíveis: PIX, CARTAO, CEDULA")
        tipo = input("Digite a modalidade de pagamento: ").strip().upper()

        dados = {
            "id_atendimento": id_atendimento,
            "data": data,
            "valor": valor,
            "tipo": tipo
        }

        if tipo == "PIX":
            dados["chave_pix"] = input("Digite a chave PIX: ")
        elif tipo == "CARTAO":
            dados["numero_cartao"] = input("Digite o número do cartão: ")
            dados["bandeira"] = input(
                "Digite a bandeira (ex: Visa, Mastercard): ")

        return dados

    def mostra_pagamentos(self, pagamentos):
        print("\n--- HISTÓRICO DE PAGAMENTOS ---")
        for p in pagamentos:
            print(f"Data: {p.data} | Valor Pago: R$ {p.valor_pago:.2f}")

            if hasattr(p, 'chave_pix'):
                print(f"Modalidade: PIX | Chave: {p.chave_pix}")
            elif hasattr(p, 'numero_cartao'):
                print(
                    f"Modalidade: Cartão de Crédito | Bandeira: {p.bandeira}")
            else:
                print("Modalidade: Cédula (Dinheiro em espécie)")
            print("-" * 30)

    def seleciona_pagamento(self):
        codigo = input(
            "Digite a Data (ou ID) do pagamento que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(f"\n>>> {msg}")
