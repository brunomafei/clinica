class Tela_Atendimento:
    def tela_opcoes(self):
        print("\n" + "="*30)
        print("--- MENU ATENDIMENTO ---")
        print("1 - Agendar Atendimento")
        print("2 - Alterar Atendimento")
        print("3 - Listar Atendimentos")
        print("4 - Cancelar/Excluir Atendimento")
        print("0 - Retornar")
        print("="*30)

        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            return -1

    def pega_dados_atendimento(self):
        print("\n--- DADOS DO AGENDAMENTO ---")
        cpf_paciente = input("CPF do Paciente: ")
        nome_clinica = input("Nome da Clínica: ")
        registro_profissional = input("Registro do Profissional: ")
        data = input("Data (DD/MM/AAAA): ")
        hora_inicio = input("Hora de Início: ")
        hora_fim = input("Hora de Fim: ")
        tipo = input("Tipo (Consulta, Exame, Retorno): ")

        try:
            valor_total = float(input("Valor Total: R$ "))
        except ValueError:
            print(">>> Erro: Valor deve ser numérico! Tente novamente.")
            return None

        return {
            "cpf_paciente": cpf_paciente,
            "nome_clinica": nome_clinica,
            "registro_profissional": registro_profissional,
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "tipo": tipo,
            "valor_total": valor_total
        }

    def mostra_atendimento(self, atendimentos):
        print("\n--- LISTA DE ATENDIMENTOS ---")
        for a in atendimentos:
            print(
                f"Data: {a.data} | Horário: {a.horario_inicio} às {a.horario_fim}")
            print(
                f"Tipo: {a.tipo_atendimento} | Valor Devido: R$ {a.valor_total:.2f}")
            print("-" * 30)

    def seleciona_atendimento(self):
        identificador = input(
            "Digite a DATA (ou ID) do atendimento que deseja selecionar: ")
        return identificador

    def mostra_mensagem(self, msg):
        print(f"\n>>> {msg}")
