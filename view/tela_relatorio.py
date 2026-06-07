class TelaRelatorio:

    def tela_opcoes(self):
        print("\n--- Relatórios ---")
        print("1. Clínicas com mais atendimentos")
        print("2. Atendimentos mais caros e mais baratos")
        print("3. Procedimentos mais realizados")
        print("4. Procedimentos mais caros e mais baratos")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print(" Digite um número válido!")
            opcao = -1
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_relatorio_clinicas_mais_atendimentos(self, relatorio):
        print("\n--- Relatório: Clínicas com mais atendimentos ---")
        if not relatorio:
            print("Nenhum dado encontrado para este relatório.")
            return
        for nome, quantidade in relatorio:
            print(f"Clínica: {nome} | Atendimentos: {quantidade}")

    def mostra_relatorio_atendimentos_mais_caros_eh_baratos(self, mais_caro, mais_barato):
        print("\n--- Relatório: Atendimentos mais caros e mais baratos ---")
        print(
            f"Mais caro: Clínica {mais_caro.clinica.nome} | Valor: {mais_caro.valor_total}")
        print(
            f"Mais barato: Clínica {mais_barato.clinica.nome} | Valor: {mais_barato.valor_total}")

    def mostra_relatorio_procedimentos_mais_realizados(self, relatorio):
        print("\n--- Relatório: Procedimentos mais realizados ---")
        if not relatorio:
            print("Nenhum dado encontrado para este relatório.")
            return
        for descricao, quantidade in relatorio:
            print(f"Procedimento: {descricao} | Quantidade: {quantidade}")

    def mostra_relatorio_procedimentos_mais_caros_eh_baratos(self, mais_caro, mais_barato):
        print("\n--- Relatório: Procedimentos mais caros e mais baratos ---")
        print(f"Mais caro: {mais_caro.descricao} | Custo: {mais_caro.custo}")
        print(
            f"Mais barato: {mais_barato.descricao} | Custo: {mais_barato.custo}")
